import cv2
import os

class EyeAnnotator:
    def __init__(self, folder_path):
        self.images = [os.path.join(folder_path, img) for img in os.listdir(folder_path) if img.endswith(('jpg', 'png'))]
        self.current_image_idx = 0
        self.clicks = 0
        self.eye_points = []

    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # Si ya hemos hecho 2 clicks (para 2 ojos), reseteamos el contador y cambiamos la imagen.
            if self.clicks >= 2:
                self.save_annotations()
                self.eye_points = []
                self.clicks = 0
                self.current_image_idx += 1
                if self.current_image_idx >= len(self.images):
                    cv2.destroyAllWindows()
                    return
                
            top_left = (x - 100, y - 100)
            bottom_right = (x + 100, y + 100)
            cv2.rectangle(self.img, top_left, bottom_right, (0, 255, 0), 1)
            self.eye_points.append((x, y))
            cv2.imshow('Image Annotation', self.img)
            self.clicks += 1

    def save_annotations(self):
        with open("annotations.txt", "a") as file:
            for point in self.eye_points:
                file.write(f"{self.images[self.current_image_idx]} {point[0]-10} {point[1]-10} 20 20\n")

    def start(self):
        cv2.namedWindow("Image Annotation")
        cv2.setMouseCallback("Image Annotation", self.click_event)
        
        while self.current_image_idx < len(self.images):
            self.img = cv2.imread(self.images[self.current_image_idx])
            cv2.imshow("Image Annotation", self.img)
            cv2.waitKey(0)
        
        cv2.destroyAllWindows()

if __name__ == "__main__":
    folder_path = "/home/nick/titulo"  # Cambia esto por la dirección de tu carpeta
    annotator = EyeAnnotator(folder_path)
    annotator.start()
