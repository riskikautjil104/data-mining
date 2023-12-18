# data = {'data1':([1,2,4],[2,5,1])}

# print(data['data1'][0][0])


import cv2
import mediapipe as mp 
import time

cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)

