import cv2
import os

def read_directory(directory_name):
    for filename in os.listdir(directory_name):
        print(filename)  # 仅仅是为了测试
        img = cv2.imread(directory_name + "/" + filename)
        cv2.imshow(filename, img)
        cv2.waitKey(0)
        cv2.imwrite("D:\PythonSpace\pythonIPR\PhotoSave" + "/" + filename, img)
        return filename

read_directory("D:\csm")