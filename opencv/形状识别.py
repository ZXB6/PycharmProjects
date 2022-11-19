import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import scipy.fftpack as fft


path_pic = "./pic"
filename = os.listdir(path_pic)

if not os.path.exists(path_result):
    os.mkdir(path_result)

for i in range(len(filename)):
    image = cv2.imread(path_pic + "/" + filename[i], 0)
    ret, thresh = cv2.threshold(image, 100, 255, 0)

    #计算轮廓
    out, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros(image.shape) + 255
    imgnew = cv2.drawContours(drawing, contours, 1, (0, 255, 255), 0)

    #确定轮廓的重心
    mu = cv2.moments(contours[1])
    cx = int(mu['m10']/mu['m00'])  #表示列数，是横坐标
    cy = int(mu['m01']/mu['m00'])

    #计算轮廓到重心的距离
    label = np.where(drawing == 0)
    #注意此处矩阵元素的下标与在二维平面的坐标是反的，行表示纵坐标
    location = np.array(label).T
    location = location[:, ::-1]
    location = location.astype("int64")
    center = np.array([[cx, cy]])
    center = np.tile(center, (location.shape[0], 1))
    center = center.astype("int64")
    dist = (location - center)**2
    dist = np.sqrt(dist.sum(axis=1))

    up = location[:, 1] <= cy   #注意在重心以上，对应纵坐标是小
    down = location[:, 1] > cy
    location_up = location[up, :]
    location_down = location[down, :]
    dist_up = dist[up]
    dist_down = dist[down]
    angle_up = location_up[:, 0] - cx
    angle_up = np.arccos(angle_up / dist_up)
    angle_down = location_down[:, 0] - cx
    angle_down = np.arccos(angle_down / dist_down) * (-1) + np.pi * 2
    location = np.vstack((location_up, location_down))
    dist = np.hstack((dist_up, dist_down))
    angle = np.hstack((angle_up, angle_down))
    order = np.argsort(angle, axis=0)
    dist = dist[order]
    location = location[order]
    angle = angle[order]


    plt.figure()
    plt.plot(angle, dist / max(dist))
    plt.title(filename[i])
    plt.ylim(0, 1.2)
    plt.savefig(path_result + "/" + filename[i])
    plt.close()

    # 离散DCT
    time_domain = fft.dct(dist / max(dist))
    plt.figure()
    plt.plot(np.arange(0, 20, 1), np.abs(time_domain)[0:20])
    plt.xticks(np.arange(20))
    plt.title(filename[i])
    plt.savefig(path_result + "/ifft_" + filename[i])
    plt.close()

    # 差分
    diff_1 = np.gradient(dist / max(dist))
    diff_2 = np.gradient(dist / max(dist), 2)
    plt.figure()
    plt.plot(np.arange(0, diff_1.shape[0], 1), diff_1)
    plt.plot(np.arange(0, diff_2.shape[0], 1), diff_2)
    plt.title(filename[i])
    plt.legend(["order_1", "order_2"])
    plt.plot(np.arange(0, diff_2.shape[0], 1), 0*np.arange(0, diff_2.shape[0], 1))
    plt.savefig(path_result + "/diff_" + filename[i])
    plt.close()


    print(i)


    # cv2.circle(drawing, (cx, cy), 2, (0, 255, 255), -1)
    # cv2.imwrite(path_result + "/contour_" + filename[i], drawing)
    # cv2.waitKey(1000)
    # cv2.destroyAllWindows()

