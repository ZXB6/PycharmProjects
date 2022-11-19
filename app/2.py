from pyzbar import pyzbar
import cv2,os,numpy as np

i = a = b = 0
print("waiting")
file_name='D:\c'
for pic_name in os.listdir(file_name):
        #img = cv2.imread(file_name + "/" +pic_name, cv2.IMREAD_UNCHANGED)
        img = cv2.imdecode(np.fromfile(file_name + "/" +pic_name,dtype=np.uint8),-1)
        i+=1
        if i % 100==0 : print("已处理%d张"%i)
        barcodes = pyzbar.decode(img)
        for barcode in barcodes:
            points = []
            for point in barcode.polygon:
                points.append([point[0], point[1]])
            cv2.polylines(img, [np.array(points, dtype=np.int32).reshape(-1, 1, 2)], isClosed=True, color=(0, 0, 255),
                          thickness=2)
            text = "({}): {} ".format(barcode.type, barcode.data.decode("UTF-8"))
            if "https://jkkgzh.hnhfpc.gov.cn/hunan" in text:
                a += 1
            else:
                b += 1
                print(pic_name)
                continue
print(" ")
print("成功扫描 %d 张场所码，失败 %d张   失败文件名如上" % (a, b))

# read_directory("C:\Users\asus\PycharmProjects\pythonProject\app\场所码")
# img2 = cv2.imread("01ca90a58b55dd0b617a726b5fc56103.jpg")
# image_detect(img2)

