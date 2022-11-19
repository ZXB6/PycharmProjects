import cv2
import numpy as np
import matplotlib.pyplot as plt

def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    # print(image.shape)                                                        # 检查roi区域
    y1 = image.shape[0]
    y2 = int(y1 * (4/5))                                                        # 取1/5的显示区域
    x1 = int((y1 - intercept) / slope)                                          # y = mx + b->x = (y - b)/m
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])

 # 求平均，优化线条
def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)          # 1次拟合次
        # print(parameters)                                       # 检测斜率和截距
        slope = parameters[0]                                    # 接收斜率
        intercept = parameters[1]                                # 接收截距
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    # print(left_fit)
    # print(right_fit)
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    # print(left_fit_average, 'left')
    # print(right_fit_average, 'right')
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    return np.array([left_line, right_line])

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)            # Gaussian滤波，(5, 5)表示高斯矩阵的长与宽都是5，标准差取0
    canny = cv2.Canny(blur, 50, 150)
    return canny

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:                                                           # 检测列阵是否为空
        # for line in lines:
        #     # print(line)                                                            # 查看维度，这里为二维
        #     x1, y1, x2, y2 = line.reshape(4)
        for x1, y1, x2, y2 in lines:
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 5)               # BGR
    return line_image

def region_of_interst(image):
    height = image.shape[0]               # 取图像的垂直尺寸(高度),这里作为图片的底部
    polygons = np.array([
    [(150, height), (1200, height), (712, 682)]             # 70 (550, 310)
    ])
    mask = np.zeros_like(image)             # 设一个全是0的单位矩阵
    cv2.fillPoly(mask, polygons, 255)           # 把指定区域变为255，实现分割
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

image = cv2.imread('test_image.png')
lane_image = np.copy(image)
canny_image = canny(lane_image)
cropped_image = region_of_interst(canny_image)
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 10, np.array([]), minLineLength=40, maxLineGap=5)          # https://blog.csdn.net/e01528/article/details/82749816
averaged_lines = average_slope_intercept(lane_image, lines)
line_image = display_lines(lane_image, averaged_lines)
# cv2.imshow('result',image)                                                                    # 输出原图像对比
combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)                                # 图像的加权和（混合、融合）,cv2.addWeigthted(src1,a,src2,b,c),图像1×系数1+图像2×系数2+亮度调节量”
cv2.namedWindow("result", 0)
cv2.resizeWindow("result", 1200, 900)
cv2.imshow('result', combo_image)
cv2.waitKey(0)

# plt.imshow(canny_image)             #测试公路所在区间
# plt.show()

# cap = cv2.VideoCapture("202112061138.mp4")
# while(cap.isOpened()):
#     _, frame = cap.read()
#     canny_image = canny(frame)
#     cropped_image = region_of_interst(canny_image)
#     lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 10, np.array([]), minLineLength=40, maxLineGap=5)
#     averaged_lines = average_slope_intercept(frame, lines)
#     line_image = display_lines(frame, averaged_lines)
#     combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
#     cv2.imshow('result', combo_image)
#     cv2.waitKey(1)
