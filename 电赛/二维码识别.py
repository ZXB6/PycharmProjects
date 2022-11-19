# 功能：使用pyzbar库识别条形码和二维码通用
import cv2
import pyzbar.pyzbar as pyzbar

# 二维码识别函数
# 返回参数：image标记后的图像矩阵;C_x,C_y：目标二维码中心点坐标；
# （返回参数：flag：等于1时表示成功检测到二维码，0表示未成功检测）
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
    return image, 320, 240  # 返回默认图像中心位置


cap = cv2.VideoCapture(1)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

if __name__ == '__main__':
    while cap.isOpened():
        ret, frame = cap.read()
        # frame = cv2.resize(frame, (160, 120))
        img, x, y = decodeDisplay(frame)
        cv2.imshow('imgage', img)
        cv2.waitKey(2)
