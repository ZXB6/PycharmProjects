import cv2 ,numpy as np
import pyzbar.pyzbar as pyzbar
cap=cv2.VideoCapture(0)
# 寻找竖直黑色直线并标记  输出参数：黑色直线x轴坐标
def black_line(image):
    # cv2.imshow('line_image', image)
    # 设置闸值，只寻找黑色直线
    Lower = np.array([90, 0, 0])
    Upper = np.array([180, 255, 46])
    HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(HSV, Lower, Upper)
    # lines = cv2.HoughLines(mask, 1, np.pi/180, threshold=400, max_theta=0.1)
    lines = cv2.HoughLines(mask, 1, np.pi/180, threshold=20, max_theta=0.5)
    # print('lines', lines)
    # 判断是否检测到直线
    if lines is not None:
        for line in lines:
            r, theta = line[0]
            # 画出垂直直线
            if theta<0.1:
                x0 = r * np.cos(theta)
                y0 = r * np.sin(theta)
                x1 = int(x0 - 1000 * np.sin(theta))
                y1 = int(y0 + 1000 * np.cos(theta))
                x2 = int(x0 + 1000 * np.sin(theta))
                y2 = int(y0 - 1000 * np.cos(theta))
                # cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                # cv2.imshow('line_image', image)
                x = abs((x1+x2)/2)
                print('黑色直线位置', x)
                return x
    x = 0
    return 0  # 返回0代表识别直线失败


# 基于条形码的黄色值进行识别
# 输入参数：image输入图像矩阵
# 输出参数：条形码中央的坐标
def decodeDisplay(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转换成灰度图
    barcodes = pyzbar.decode(image)
    if barcodes != []:
        print('成功检测二维码')
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cx = int(x + w / 2)
        cy = int(y + h / 2)
        cv2.circle(image, (cx, cy), 2, (0, 255, 0), 8)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        print('position', cx, cy)
        # cv2.imwrite('G:/'+str(x)+'.jpg', image)
        return image, cx, cy
    cx = 0
    cy = 0
    return cx, cy  # 返回值都为零表示未识别
while True:
    success,img = cap.read()
    black_line(img)
    decodeDisplay(img)
    cv2.imshow("s", img)
    cv2.waitKey(1)