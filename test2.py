# -*- coding: utf-8 -*-
#이거는 이미지를 얻어와서 그대로 이미지를 뿌려주는것 
import numpy as np
import cv2
#from matplotlib import pyplot as plt
import os
##샾 두개는 카메라를 키거나 영상 이용시 사용할 코드이다.

face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/cctv/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('/home/pi/Desktop/cctv/opencv-master/data/haarcascades/haarcascade_fullbody.xml')

##cam = cv2.VideoCapture('/home/pi/Desktop/cctv/Me.h264')

##cam.set(3, 640) # set video widht

##cam.set(4, 480)


image = cv2.imread('/home/pi/Desktop/cctv/test.png') #이미지 경로로부터 불러오기 여기서 나로 인식할 사람이랑 아닌 사람의 사진을 로드하는걸 결정하면 된다. (minjung=test.png, none=testnone.png)
#사진 크기 줄이는 것도 고려해야한다.

#image=cv2.resize(image, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) #자꾸 오류떠서 그냥 화면 크기 맞춰주기(사진한정) 얘를 지우면 내이름이 출력되네..?

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #그레이 색상으로 화면 바꿔주기 (인식용.)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/pi/Desktop/cctv/trainer/trainer2.yml')

font = cv2.FONT_HERSHEY_SIMPLEX

id=0

names = ['None', 'loze', 'junyoung', 'minjung', 'minjung']

#image = cv2.imread('/home/pi/Desktop/cctv/test.png')


#while True:

#for (x,y,w,h) in body:
#while True:
#while(cam.isOpened()):

##ret, image = cam.read()

    
#while (True):    
    
body = body_cascade.detectMultiScale(grayImage, 1.03, 5) ##여기가 제일 문제많이 생김 

for (x,y,w,h) in body:
    
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)
    body_image_gray = grayImage[y:y+h, x:x+w]

    body_image_color = image[y:y+h, x:x+w]
    
    faces_in_body = face_cascade.detectMultiScale(body_image_gray, 1.03, 5)

    for (fx,fy,fw,fh) in faces_in_body:
        
        cv2.rectangle(body_image_color,(fx,fy),(fx+fw,fy+fh),(0,255,255),2)
            
        id, confidence = recognizer.predict(body_image_gray[y:fy+fh,x:fx+fw]) ##여기가 제일 문제많이 생김 바디는 인식했는데 얼굴은 인식 못한경우 
            
        
        if (100-confidence >= 55):

            id = names[id] #사람의 이름 그니까 

            confidence = "  {0}%".format(round(100 - confidence)) #만약 정확도가 100이하라면 100에서 정확도를 뺴서 인식도를 나타내라
            
            cv2.putText(image, str(id), (fx+5,fy-5), font, 1, (255,255,255), 2) #사람이름 이름 출력 

            cv2.putText(image, str(confidence), (fx+5,fy+fh-5), font, 1, (255,255,0), 1)  #정확도 퍼센트 출력
                
            break
            
            
        elif (100-confidence < 55) :
            
            face_img = image[y:fy+fh, x:fx+fw] # 인식된 얼굴 이미지 crop

            face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.04, fy=0.04) # 축소

            face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA) # 확대
        
            image[y:y+h, x:x+w] = face_img
                
            break
                
        

 

#plt.figure(figsize=(12,12))
#plt.imshow('camera',image)
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()



    cv2.imshow('camera',image) #화면출력 

cv2.waitKey(0) #얘로인해서 화면이 안나올 일은 없음 
cv2.destroyAllWindows()#누르면 꺼짐 

##cam.release() 

