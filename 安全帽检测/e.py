import cv2
import numpy as np
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
while True:
      success, frame = cap.read()
      if not success:
         # 摄像头读取失败
         print("failed to read video")
         continue

      image = frame
      result = image.copy()

      faces = face_cascade.detectMultiScale(image, scaleFactor=1.3, minNeighbors=5, minSize=(40, 40))
      eyes = eye_cascade.detectMultiScale(image, 1.3, 10)

      layers = cv2.split(image)
      feature = cv2.subtract(layers[-1], layers[0])
      success, feature = cv2.threshold(feature, 175, 255, cv2.THRESH_BINARY)

      valid_faces = []
      valid_eyes_pairs = []
      if len(eyes) >= 2:
          # 检测是否有两个有效的眼睛，如果有就说明检测成功
          sort_eyes = sorted(eyes, key=lambda i: i[0] + i[2] // 2)
          eyes_center = [(i[0] + i[2] // 2, i[1] + i[3] // 2) for i in sort_eyes]
          for i in range(len(eyes_center) - 1):
                left_eye = sort_eyes[i]
                left_eye_center = eyes_center[i]

                for j in range(i+1, len(eyes_center)):
                      right_eye = sort_eyes[j]
                      right_eye_center = eyes_center[j]

                      area_diff = abs(right_eye[2] * right_eye[3] - left_eye[2] * left_eye[3]) / max(right_eye[2] *
                                 right_eye[3], left_eye[2] * left_eye[3])
                      y_diff = abs(right_eye_center[1] - left_eye_center[1])
                      x_diff = right_eye_center[0] - left_eye_center[0]

                      if area_diff < 0.6 and x_diff > 60 and y_diff < 20:
                            valid_eyes_pairs.append([left_eye, right_eye])
      # 开始检测头盔
      if not len(valid_eyes_pairs) and not len(valid_faces):
          cv2.putText(result, "error detect person face!", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
      else:
            # 开始检测头顶是否有头盔
            if len(valid_eyes_pairs):
                left_eye, right_eye = valid_eyes_pairs[0]
                left_eye_center = (left_eye[0] + left_eye[2] // 2, left_eye[1] + left_eye[3] // 2)
                right_eye_center = (right_eye[0] + right_eye[2] // 2, right_eye[1] + right_eye[3] // 2)

                eyebrow = ((left_eye_center[0] + right_eye_center[0]) // 2, (left_eye_center[1] +
                                                                             right_eye_center[1]) // 2)
                direct_distance = ((left_eye_center[0] - right_eye_center[0]) ** 2 +
                                   (left_eye_center[1] - right_eye_center[1]) ** 2) ** (1 / 2)
                helmet_center = (eyebrow[0], int(eyebrow[1] - direct_distance * 1.05))
                cv2.ellipse(result, helmet_center, (150, 120), 0, 180, 360, color=(255, 255, 0), thickness=2)

                # 获得特征层红色的占头上一块区域的比例
                mask = np.zeros(image.shape[:2], dtype=np.uint8)
                cv2.ellipse(mask, helmet_center, (150, 120), 0, 180, 360, color=255, thickness=-1)

                roi_pixel_num = np.sum(mask == 255)
                roi_valid_binary = cv2.bitwise_and(feature, mask)  # 像素值进行二进制“与”操作
                roi_valid_pixel_num = np.sum(roi_valid_binary == 255)
                ratio = roi_valid_pixel_num / roi_pixel_num

                print(ratio)
                if ratio > 0.3:
                    cv2.putText(result, str(ratio) + "have helmet", (50, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
                else:
                    cv2.putText(result, "have no helmet", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

      cv2.imshow("result", result)
      key = cv2.waitKey(1)
      # 检测到两个人眼就保存
      if len(eyes) >= 2:
            cv2.imwrite("success.png", image)
      # 如果带了头盔人眼检测存在问题没办法检测到 按下q 进行图片保存打卡
      if key == ord("q"):
            cv2.imwrite("test.png", image)
