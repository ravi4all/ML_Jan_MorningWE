import numpy as np
import cv2
from math import *

face = np.load('facedata.npy')
labels = np.load('facelabels.npy')

#print(labels)
#print(face)

print("Before",face.shape)
face = face.reshape(face.shape[0], face.shape[1] * face.shape[2])
print("After",face.shape)

cap = cv2.VideoCapture(0)
dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

font = cv2.FONT_HERSHEY_SIMPLEX

def recognize_face(img):
    im = cv2.resize(img,(100,100))
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im = im.flatten()

    def dist(x1,x2):
        #return sqrt(sum(pow(x1-x2,2)))
        return np.sqrt(((x1-x2)**2).sum())

    #X_train = face, x = im, y_train = labels
    def knn(X_train, x, y_train, k = 7):
        vals = []

        for i in range(X_train.shape[0]):
            v = [dist(x, X_train[i,:]), y_train[i]]
            vals.append(v)

        updated_vals = sorted(vals, key = lambda x : x[0])
        pred_arr = np.asarray(updated_vals[:k])
        pred_arr = np.unique(pred_arr[:, 1], return_counts = True)
        pred = pred_arr[1].argmax()
        return pred_arr[0][pred]


    result = knn(face, im, labels, 7)

    return result

while True:
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print gray.shape
    faces = dataset.detectMultiScale(gray, 1.3, 5)

    for x,y,w,h in faces:
        fc = img[x:x+w, y:y+h, :]
        output = recognize_face(fc)
        cv2.putText(img, output, (x, y), font, 1, (255, 255, 0), 2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('rgb', img)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
