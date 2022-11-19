import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
  # 获取每一帧
  ret,frame=cap.read()
  # 转换到HSV
  hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
  # 设定蓝色的阈值
  lower_blue=np.array([110 , 50 , 50])
  upper_blue=np.array([130 , 255, 255])
  # 根据阈值构建掩模
  mask=cv2.inRange(frame,lower_blue,upper_blue)
  # 对原图像和掩模进行位运算
  res=cv2.bitwise_and(frame,frame,mask=mask)

  # 显示图像
  cv2.imshow('frame',frame)
  cv2.imshow('mask',mask)
  cv2.imshow('res',res)
  cv2.waitKey(1)
