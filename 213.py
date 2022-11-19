# -*- coding:utf-8 -*-
import numpy as np
import cv2
import cv2.aruco as aruco
import glob
import imutils
import time
import V_Display as vd
import V_UCom as com

mtx = np.array([
    [235.30964269, 0, 110.68578335],
    [0, 229.75119518, 107.7683592],
    [0, 0, 1],
])
dist = np.array([-0.57063508, 0.8469956, -0.00954837, 0.00477835, -0.47724227])
cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)
center_x = 160
center_y = 120
print("start reading video...")
time.sleep(2.0)
print("start working")
vd.init()

Uart_buf = bytearray([0x55, 0xAA, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0xAA])
com.init(mode=2)


def convey(list):
    postion_ids = int(list[0])
    postion_x = int(list[1])
    postion_y = int(list[2])
    print(list)
    Uart_buf = bytearray(
        [0x55, 0xAA, 0x10, (postion_x & 0xff00) >> 8, postion_x & 0x00ff, (postion_y & 0xff00) >> 8, postion_y & 0x00ff,
         0x00, 0x00, 0x00, 0x00, 0xAA])
    com.send(Uart_buf)


while (True):
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=160)
    # operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()

    # lists of ids and the corners beloning to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    font = cv2.FONT_HERSHEY_SIMPLEX  # font for displaying text (below)

    if np.all(ids != None):
        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners[0], 0.05, mtx,
                                                        dist)  # Estimate pose of each marker and return the values rvet and tvec---different from camera coefficients
        # (rvec-tvec).any() # get rid of that nasty numpy value array error

        aruco.drawDetectedMarkers(frame, corners, ids)
        if ids[0][0] == 12:
            aruco.drawAxis(frame, mtx, dist, rvec[0], tvec[0], 0.1)

        numbers = ids.shape[0]
        send = np.zeros([numbers, 3], dtype=float)
        for t in range(numbers):

            a = corners[t]
            x1 = a[0][1][0]
            y1 = a[0][1][1]
            x2 = a[0][2][0]
            y2 = a[0][2][1]
            x3 = a[0][3][0]
            y3 = a[0][3][1]
            x4 = a[0][0][0]
            y4 = a[0][0][1]
            try:
                k1 = (y3 - y1) / (x3 - x1)
                b1 = (x3 * y1 - x1 * y3) / (x3 - x1)
                k2 = (y4 - y2) / (x4 - x2)
                b2 = (x4 * y2 - x2 * y4) / (x4 - x2)
                x5 = -(b1 - b2) / (k1 - k2)
                y5 = k1 * x5 + b1
                send[t][0] = ids[t][0]
                send[t][1] = int(x5)
                send[t][2] = int(y5)
                convey(send[t])
            except:
                print("error=1")

        print(send)

    vd.show(frame)