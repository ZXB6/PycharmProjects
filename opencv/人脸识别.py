import cv2
cap=cv2.VideoCapture(0)
while True:
    success,img = cap.read()
# 导入人脸级联分类器引擎，'.xml'文件里包含训练出来的人脸特征
    face_engine = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# 用人脸级联分类器引擎进行人脸识别，返回的faces为人脸坐标列表，1.3是放大比例，5是重复识别次数
    faces = face_engine.detectMultiScale(img,scaleFactor=1.3,minNeighbors=5)

# 对每一张脸，进行如下操作
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.putText(img, "human", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow('img2',img)
    cv2.waitKey(1)
    #cv2.imwrite('output.jpg',img)
