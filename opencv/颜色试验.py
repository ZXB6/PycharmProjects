import cv2

cap = cv2.VideoCapture(0)

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print("面积", area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # 图形轮廓，控制权，轮廓指数，
            peri = cv2.arcLength(cnt, True)
            print("周长", peri)
            approx = cv2.approxPolyDP(cnt, 0.1*peri, True)
            print(len(approx))
            objCor = len(approx)
            # 物体角
            x, y, w, h = cv2.boundingRect(approx)
            # 边界矩形
            if objCor == 3: objectType ="Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                # 纵横比
                if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
                else:objectType="Rectangle"
            elif objCor > 4: objectType= "Circles"
            else:objectType="None"

            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, # 比例尺
                        (0, 0, 0), 2)

while True:
    success, imgContour = cap.read()
    imgGray = cv2.cvtColor(imgContour, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    getContours(imgCanny)
    cv2.imshow("Video", imgContour)
    cv2.waitKey(1)
