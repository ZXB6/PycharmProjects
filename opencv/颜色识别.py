import cv2
import numpy as np
# purple=(125, 43, 46,155, 255, 255)
# black = (0, 0, 0, 180, 255, 46)
# gray =(0,0,46,180,43,220)
# white =(0,0,221,180,30,255)
# red = (0/156,43,46,10/180,255,255)
# yellow = (18, 0, 196, 36, 255, 255)
# green = (35,40,40, 77, 255, 255)
# blue = (100,43,46, 124, 255, 255)
# orange = (11,43,46,25,255,255)不清楚
cap = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)
while True:
    success, img = cap.read()
    frameHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    colorLow = np.array([0, 43, 46])  # B  G  R
    color= (0, 0, 255)
    colorHigh = np.array([10, 255, 255])
    mask = cv2.inRange(frameHSV, colorLow, colorHigh)
    # dilation = cv2.dilate(img, kernel, iterations=1)# 膨胀操作
    # closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)# 闭操作
    # closing = cv2.GaussianBlur(closing, (5, 5), 0)# 高斯滤波
    # edges = cv2.Canny(closing, 120, 255)  # 边缘检测
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 方法
    # 查找所有轮廓
    #img = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    # 查找最大轮廓
    # contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    # biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
    # img = cv2.drawContours(img, biggest_contour, -1, (0, 255, 0), 2)
    # 边界矩形


    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
    x, y, w, h = cv2.boundingRect(biggest_contour)
    img=cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    img=cv2.putText(img, 'red', (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, color, 2)
    cv2.imshow(" ", img)
    cv2.waitKey(1)
