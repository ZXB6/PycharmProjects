import cv2
import numpy as np

cap = cv2.VideoCapture(0)
imgTarget = cv2.imread('TargetImage.jpg')
myVid = cv2.VideoCapture('video.mp4')
imgTarget =cv2.resize(imgTarget,(250,250))
success, imgVideo = myVid.read()
hT, wT, cT = imgTarget.shape
#imgVideo = cv2.resize(imgVideo, (wT, cT))

orb = cv2.ORB_create(nfeatures=1000)
kp1, des1 = orb.detectAndCompute(imgTarget, None)
#imgTarget = cv2.drawKeypoints(imgTarget,kp1,None)

while True:
    sucess, imgWebcam = cap.read()
    kp2, des2 = orb.detectAndCompute(imgWebcam, None)
    #imgWebcam = cv2.drawKeypoints(imgWebcam, kp2, None)
    bf=cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)
    print(len(good))
    imgFeatures = cv2.drawMatches(imgTarget, kp1, imgWebcam, kp2, good, None, flags=2)
    cv2.imshow('imgFeatures', imgFeatures)
   # cv2.imshow('Webcam', imgWebcam)
    cv2.imshow('ImgTarget',imgTarget)

    cv2.waitKey(1)