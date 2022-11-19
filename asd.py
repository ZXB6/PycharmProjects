import numpy as np
import cv2
import time
import os
import math
#增加了底层驱动，可以直接通过cv2的0号设备读取摄像头
cap = cv2.VideoCapture(0)
cap.set(3,320)#设置摄像头输出宽
cap.set(4,240)#设置摄像头输出高
print("start reading video...")
time.sleep(2.0)
print("start working")

def getContours(img):
    objectType=""
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 2)
            # 图形轮廓，控制权，轮廓指数，
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.1*peri, True)
            objCor = float(len(approx))
            # 物体角
            x, y, w, h = cv2.boundingRect(approx)
            a=(w+h)*math.pi /peri/2
            density = area / ((w+8) * (h+8))
            circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50, param1=80, param2=20, minRadius=30, maxRadius=100)
            if objCor == 3 and density > 0.4: objectType ="Tri"
            elif objCor >= 4 and density <0.785 and density >0.65 and a >0.78:
                 if circles is not None:objectType = "circle"
            elif objCor == 4 and density > 0.475:
                     aspRatio = w / float(h)
                     if aspRatio > 0.92 and aspRatio < 1.04:objectType = "Square"
                     else:objectType = "Rectangle"
            else:objectType = "None"
            cv2.rectangle(imgContour, (x-4, y-4), (x+w+4, y+h+4), (0, 255, 0), 2)
            #cv2.putText(imgContour, objectType,(x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7,(0, 0, 0), 2)
            print(objectType)
while True:
    success, imgContour = cap.read()
    imgGray = cv2.cvtColor(imgContour, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    getContours(imgCanny)
    cv2.imshow("Video", imgContour)
    cv2.waitKey(1)
