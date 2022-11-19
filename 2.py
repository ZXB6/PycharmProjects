import cv2
import math
cap = cv2.VideoCapture(0)


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
        # 图形轮廓，控制权，轮廓指数，
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.1 * peri, True)
        objCor = len(approx)
        x, y, w, h = cv2.boundingRect(approx)
        density=area/w*h
        if density>0.805:# 理论上矩形和他的外接矩形应该是完全重合
            print("检测为长方形  "+str(density))
        elif density>0.65:
            print("检测为圆  "+str(density))
        elif density>0.40:
            print("检测为三角型  "+str(density))
        else:
            print("no dectedtion")
        # 边界矩形
        if objCor == 3:
            objectType = "Tri"
        elif objCor == 4:
            aspRatio = w / float(h)
            if aspRatio > 0.98 and aspRatio < 1.03:
                objectType = "Square"
            else:
                objectType = "Rectangle"
        elif objCor > 4:
            objectType = "Circles"
        else:
            objectType = "None"

        cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(imgContour, objectType,
                    (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,  # 比例尺
                    (0, 0, 0), 2)

while True:
    success, imgContour = cap.read()
    imgGray = cv2.cvtColor(imgContour, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    getContours(imgCanny)
    cv2.imshow("Video", imgContour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
