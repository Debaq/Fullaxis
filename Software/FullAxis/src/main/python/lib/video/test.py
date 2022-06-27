import cv2

vid = cv2.VideoCapture(0)


serialNum = vid.get(cv2.CAP_PROP_MONOCHROME)
print(serialNum)