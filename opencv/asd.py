import cv2
import numpy as np
cap=cv2.VideoCapture(0)
#小球颜色识别bgr
def colour2(img_b,img_g,img_r) :
    if ((img_b>=60 and img_b<=130 )  and (img_g>=60 and img_g<=130) and (img_r>=140 and img_r<=220) ):
        cv2.putText(origin,'red', (i[0]-i[2],i[1]-i[2]), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
    elif ((img_b>=70 and img_b<=140) and (img_g>=120 and img_g<=190) and (img_r>=170 and img_r<=240) ):
        cv2.putText(origin,'yellow',(i[0]-i[2],i[1]-i[2]), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
    elif ((img_b>=70 and img_b<=140) and (img_g>=150 and img_g<=230) and (img_r>=100 and img_r<=170) ):
        cv2.putText(origin,'green', (i[0]-i[2],i[1]-i[2]), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2) 
    elif ((img_b>=50 and img_b<=120) and (img_g>=60 and img_g<=120) and (img_r>=70 and img_r<=120) ):
        cv2.putText(origin,'brown', (i[0]-i[2],i[1]-i[2]), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)

while(True):
    clear_output(wait=True)
    success, imgMat = cap.read()
    origin = cv2.resize(imgMat, (320,240))
    start = time.time() 
    # 转换为灰度图 
    img_gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
    # medianBlur 平滑（模糊）处理
    img_gray = cv2.medianBlur(img_gray, 7)
    #圆检测
    circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, 40, param1=50,param2=35, minRadius=0, maxRadius= 300)    
    if circles is None:
        pass
    else:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # 勾画正方形，origin图像、i[2]*2是边长
            cv2.rectangle(origin,(i[0]-i[2],i[1]-i[2]),(i[0]+i[2],i[1]+i[2]),(255,0,0), 2)
            #取球心一小块区域
            roi = origin[i[0]:i[1] , i[0]:i[1]+1] 
            #分离bgr通道
            img_b = np.uint16(np.mean(roi[:,:,0]))
            img_g = np.uint16(np.mean(roi[:,:,1]))
            img_r = np.uint16(np.mean(roi[:,:,2]))
            #判断小球颜色
            colour2(img_b,img_g,img_r)

# 计 算 消 耗 时 间
    end = time.time()   
    ps.CommonFunction.show_img_jupyter(origin)
    print(end - start)
