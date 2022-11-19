import cv2 ,numpy as np

cap=cv2.VideoCapture(0)
# 寻找竖直黑色直线并标记
# 输入参数：image输入图像矩阵
# 输出参数：黑色直线x轴坐标
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
def yellow_code(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 设定黄色的闸值
    lower_yellow = np.array([20, 40, 100])
    upper_yellow = np.array([60, 150, 255])
    # 根据闸值构建掩模
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # 进行开运算和闭运算
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

    conts, hier = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 找出边界

    cv2.drawContours(image, conts, -1, (0, 255, 0), 3)  # 画出边框

    # 显示图像
    cv2.imshow('image', image)
    if conts:
        print('成功检测到条形码！')
        cnts = conts[0]
        area = cv2.contourArea(cnts)
        # print('area', area)
        # 设定面积闸值，排除黄色小噪点影响
        if area > 150:
            M = cv2.moments(cnts)
            cx = int(M["m10"] / (M["m00"]))
            cy = int(M["m01"] / (M["m00"]))
            print('条形码位置', cx, cy)
            # cv2.circle(image, (cx, cy), 3, (0, 0, 255), thickness=-1)
            # cv2.imshow('image', image)
            return cx, cy
    cx = 0
    cy = 0
    return cx, cy  # 返回值都为零表示未识别
while True:
    success,img = cap.read()
    #black_line(img) cv2.imshow("s",img)
    yellow_code(img)
    cv2.waitKey(1)