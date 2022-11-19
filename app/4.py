from pyzbar import pyzbar
import cv2,os
import numpy as np

# cap = cv2.VideoCapture(0)
def read_picture(file_name):
    i = 0
    for pic_name in os.listdir(file_name):
        img = cv2.imread(file_name + "/" +pic_name, cv2.IMREAD_UNCHANGED)
        i+=1
        print(i)
        image_detect(img,pic_name)

def image_detect(img):
    QRdetecter = cv2.QRCodeDetector()
    barcodes = pyzbar.decode(img)
    #print(barcodes)

    for barcode in barcodes:# 循环读取检测到的条形码
        # 绘条形码、二维码多边形轮廓
        points =[]
        for point in barcode.polygon:
            points.append([point[0], point[1]])
        points = np.array(points,dtype=np.int32).reshape(-1,1, 2)
        cv2.polylines(img, [points], isClosed=True, color=(0,0,255),thickness=2)
        barcodeData = barcode.data.decode("UTF-8") #先解码成字符串
        barcodeType = barcode.type
        # 绘出图像上的条形码数据和类型
        text = "({}): {} ".format(barcodeType, barcodeData)
        print(text)


        #cv2.putText(img, text, (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        #cv2.imshow("QR", img)


# read_directory("C:\Users\asus\PycharmProjects\pythonProject\app\场所码")
img2 = cv2.imread(r"微信图片_20220310144708.png", cv2.IMREAD_UNCHANGED)
image_detect(img2)

#read_picture("D:\csm")