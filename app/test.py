import cv2
import pyzbar
import opencv.contrib.python
import opencv-python
import paddleocr
import paddlepaddle


def detect_qrcode(image, block):
    block_image, block_rect, _ = block
    block_x, block_y, _, _ = block_rect
    gray = cv2.cvtColor(block_image, cv2.COLOR_BGR2GRAY)
    qrcodes = decode(gray, [ZBarSymbol.QRCODE])
    if len(qrcodes) > 0:
        qrcode = qrcodes[0]
        qrcodeData = qrcode.data.decode("utf-8")
        x, y, w, h = qrcode.rect
        abs_x = block_x + x
        abs_y = block_y + y
        cv2.rectangle(image, (abs_x, abs_y), (abs_x + w, abs_y + h), color_marker, 2)
        return True, qrcodeData, (abs_x, abs_y, w, h)
    else:
        return False, None, None

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 135, 255, cv2.THRESH_BINARY)
# 检测轮廓，获得对应的矩形
contours = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
for i in range(len(contours)):
    block_rect = cv2.boundingRect(contours[i])

ocr = PaddleOCR()