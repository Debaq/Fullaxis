import cython
import cv2
import numpy as np
cimport numpy as np


cdef class VideoThread():
    
    def __init__(self):
        super().__init__()

    def video_open(self):
        # capture from web cam
        cap = cv2.VideoCapture(1)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        cap.set(cv2.CAP_PROP_FPS, 60)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        
        return cap


    def video_read(self, cap):
        ret, cv_img = cap.read()
        cv_img=cv2.rotate(cv_img, cv2.ROTATE_180)
        fps = cap.get(cv2.CAP_PROP_FPS)
        return ret, cv_img, fps


    def centroid_detection (self, img):
        # convert image to grayscale image
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # convert the grayscale image to binary image
        ret,thresh = cv2.threshold(gray_image,127,255,0)
        # calculate moments of binary image
        M = cv2.moments(thresh)
        # calculate x,y coordinate of center
        cdef int cX = int(M["m10"] / M["m00"])
        cdef int cY = int(M["m01"] / M["m00"])
        return (cX,cY)
        #cv2.circle(self._img, (cX, cY), 5, (255, 255, 255), -1)    

    def detect_pupil (self, img, centroid):
        cdef int x = 0
        cdef int y = 0
        cdef float radius 
        cdef int x_sum = 0
        #dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
        #dst = cv2.fastNlMeansDenoisingMulti(self._img, None, 10, 10, 7, 21)
        blur = cv2.GaussianBlur(img,(45,45),0)
        inv = cv2.bitwise_not(blur)
        thresh = cv2.cvtColor(inv, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((2,2),np.uint8)
        erosion = cv2.erode(thresh,kernel,iterations = 1)
        ret,thresh1 = cv2.threshold(erosion,210,255,cv2.THRESH_BINARY)
        cnts, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cdef int flag = 10000
        final_cnt = None
        for cnt in cnts:
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            distance = abs(centroid[0]-x)+abs(centroid[1]-y)
            if distance < flag :
                flag = distance
                final_cnt = cnt
            else:
                continue
            #(x,y),radius = cv2.minEnclosingCircle(cnt)

        (x,y),radius = cv2.minEnclosingCircle(final_cnt)
        center = (int(x),int(y))
        radius_int = int(radius)
        cv2.circle(img,center,radius_int,(255,0,0),2)
        
        pupil = (center[0],center[1],radius_int)
        data = (img, pupil)
        return data

