# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
#%matplotlib inline
face_cascade = cv2.CascadeClassifier(
    '/home/pi/Desktop/cctv/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

image = cv2.imread('/home/pi/Desktop/cctv/test.png')

image=cv2.resize(image, dsize=(300,600),interpolation=cv2.INTER_LINEAR)

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

body_cascade = cv2.CascadeClassifier('/home/pi/Desktop/cctv/opencv-master/data/haarcascades/haarcascade_fullbody.xml')
body = body_cascade.detectMultiScale(grayImage, 1.01, 10)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/pi/Desktop/cctv/trainer/trainer.yml')

font = cv2.FONT_HERSHEY_SIMPLEX

id=0

names = ['None', 'loze', 'junyoung', 'minjung', 'minjung']

#image = cv2.imread('/home/pi/Desktop/cctv/test.png')

#while True:

for (x,y,w,h) in body:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)
    
    body_image_gray = grayImage[y:y+h, x:x+w]
    body_image_color = image[y:y+h, x:x+w]
    
    faces_in_body = face_cascade.detectMultiScale(body_image_gray)

    for (fx,fy,fw,fh) in faces_in_body:
        cv2.rectangle(body_image_color,(fx,fy),(fx+fw,fy+fh),(0,255,0),2)
            
        id, confidence = recognizer.predict(grayImage[y:fy+fh,x:fx+fw])
            
        if (100-confidence  >= 10):

            id = names[id] #사람의 이름 그니까 

            confidence = "  {0}%".format(round(100 - confidence)) #만약 정확도가 100이하라면 100에서 정확도를 뺴서 인식도를 나타내라
            
            cv2.putText(image, str(id), (fx+5,fy-5), font, 1, (255,255,255), 2) #사람이름 이름 출력 

            cv2.putText(image, str(confidence), (fx+5,fy+fh-5), font, 1, (255,255,0), 1)  #정확도 퍼센트 출력 
            
        
            #elif (100-confidence <= 55) :
            
        else :
            
                #cv2.putText(image, "UNKNOWN", (fx+5,fy-5), font, 1, (255,255,255), 2)
            face_img = image[y:fy+fh, x:fx+fw] # 인식된 얼굴 이미지 crop

            face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.04, fy=0.04) # 축소

            face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA) # 확대
        
            image[y:y+h, x:x+w] = face_img
                
        
        
plt.figure(figsize=(12,12))
plt.imshow(image)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


