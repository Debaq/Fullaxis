import numpy as np
import cv2

# Inicializar la captura de video
cap = cv2.VideoCapture(2)  # Cambia a 'path/to/video.mp4' para usar un archivo de video
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))# Función para manejar eventos de clic en la ventana de OpenCV

# Lista para almacenar los puntos seleccionados
points_selected = []
point_selection_complete = False

def select_point(event, x, y, flags, params):
    global points_selected, point_selection_complete
    if event == cv2.EVENT_LBUTTONDOWN:
        points_selected.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        point_selection_complete = True

# Inicializar la captura de video

# Leer el primer frame
ret, frame = cap.read()
cv2.imshow('Frame', frame)
cv2.setMouseCallback('Frame', select_point)

# Esperar hasta que la selección esté completa
while not point_selection_complete:
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# Parámetros para el algoritmo de Lucas-Kanade
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
p0 = np.array(points_selected, dtype=np.float32).reshape(-1, 1, 2)

# Crear una máscara de imagen para dibujar en ella
mask = np.zeros_like(frame)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calcular el flujo óptico
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # Seleccionar puntos buenos
    good_new = p1[st == 1]
    good_old = p0[st == 1]

    # Dibujar los puntos de seguimiento
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), (0, 255, 0), 2)
        frame = cv2.circle(frame, (int(a), int(b)), 5, (0, 0, 255), -1)
    img = cv2.add(frame, mask)

    cv2.imshow('Frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)

cv2.destroyAllWindows()
cap.release()