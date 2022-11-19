# -*- cosding:utf-8 -*s-
import socket
import multiprocessing
import cv2
import numpy as np
import time
import os

sockimg = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockhist = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address_server = ("127.0.0.1", 6050)
address_server_hist = ("127.0.0.1", 6050)


def calcHist(image):
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    # cv2.normalize(hist,hist)
    histData = hist.flatten()
    return histData;


def imgSend(q, fps):
    # file_object = open('/home/pi/xiluna/Auto/os_pid.txt', 'w')
    # file_object.write(str(os.getpid()))
    # file_object.close()
    while (1):
        if not q.empty():
            imgs = q.get();
            result, imgencode = cv2.imencode('.jpg', imgs)
            data = np.array(imgencode)
            stringData = data.tostring()
            if (len(stringData) < 65507):
                sockimg.sendto(stringData, address_server)
            else:
                lenth = len(stringData)
                ti = lenth / 65507
                for i in range(0, ti):
                    sockimg.sendto(stringData[i * 65507:i * 65507 + 65507], address_server)
                sockimg.sendto(stringData[ti * 65507:], address_server)
            # calculate hist
            if (len(imgs.shape) == 3 and imgs.shape[2] == 3):
                b, g, r = cv2.split(imgs)
                histImgB = calcHist(b)
                histImgG = calcHist(g)
                histImgR = calcHist(r)
                histAll = histImgB + histImgG + histImgR
                histAll = np.append(histImgB, histImgG)
                histAll = np.append(histAll, histImgR)
            elif (len(imgs.shape) == 3 and imgs.shape[2] == 1):
                histAll = calcHist(imgs)
            elif (len(imgs.shape) == 2):
                histAll = calcHist(imgs)
            histData = "\x55\xaa\xab\xba" + histAll.tostring() + "\xa5\x5a\x5a\x5b"
            sockhist.sendto(histData, address_server_hist)
            times = 1.0 / fps
            time.sleep(times)
            # print times


queue = multiprocessing.Queue(maxsize=3)


def show(img):
    try:
        queue.put(img, False)
    except:
        return


def init(fps=30):
    global address_server
    global address_server_hist
    for line in open("/home/pi/xiluna/VisionCom/Host_IP.txt"):
        i = line.find('Host_IP:')
        if (i != -1):
            startIndex = i + 8
            ipString = line[startIndex:]
            address_server = (ipString, 6050)
            address_server_hist = (ipString, 6051)
    p = multiprocessing.Process(target=imgSend, args=(queue, fps))
    p.start()