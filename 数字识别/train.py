import keras
import numpy as np
import cv2

threshold = 0.65
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)
model = keras.models.load_model("model_trained.h5")

def preProcessing( img ):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255
    return img

while True:
    success, imgOriginal = cap.read()
    img = np.asarray(imgOriginal)
    img = cv2.resize(img, (32, 32))
    img = preProcessing(img)
    cv2.imshow("Processsed Image", img)
    img = img.reshape(1, 32, 32, 1)
    classIndex = int(np.argmax(model.predict(img), axis=-1))
    predictions = model.predict(img)
    probVal = np.amax(predictions)
    print(classIndex, probVal)
    if probVal > threshold:
          cv2.putText(imgOriginal, str(classIndex) + "   " + str(probVal),
                (50, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (0, 0, 255), 1)

    cv2.imshow("Original Image", imgOriginal)
    cv2.waitKey(1)