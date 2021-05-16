# -*- coding: utf-8 -*-
##이거는 카메라를 틀어서 진행시키는것 
import numpy as np
import cv2
import picamera
import os
os.environ['OPENCV_IO_MAX_IMAGE_PIXELS']=str(2**64)
import datetime
##샾 두개는 카메라를 키거나 영상 이용시 사용할 코드이다.

##savepath = '/home/pi/Desktop/cctv/savepath' #동영상저장경로
##def record():
##        with picamera.PiCamera() as camera:
##            camera.resolution = (640,480)
##            now = datetime.datetime.now()
##            filename = now.strftime('%Y-%m-%d %H:%M:%S')
##            camera.start_recording(output = savepath + '/' + filename +'.h264')##
##            camera.wait_recording(10)
##            camera.stop_recording()

##while True:
##    record() cctv역할로 카메라 촬영 기능 구동. 10초에 한번씩 동영상 촬영. 지정된 경로로 지정된 파일명으로 저장 



face_cascade = cv2.CascadeClassifier(r"/home/pi/Desktop/cctv/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(r"/home/pi/Desktop/cctv/opencv-master/data/haarcascades/haarcascade_fullbody.xml")

cam = cv2.VideoCapture('/home/pi/Desktop/cctv/savepath/2021-05-10 05:15:07.h264') #저장된 영상 재생
#cam=cv2.VideoCapture('/home/pi/Desktop/cctv/savepath/2021-05-12 16:05:05.h264')


cam.set(3, 640) # set video widht

cam.set(4, 480)

#minW = 0.1*cam.get(3)

#minH = 0.1*cam.get(4)

mozaic=cv2.imread('/home/pi/Desktop/cctv/mozaic.png')
##image = cv2.imread('/home/pi/Desktop/cctv/test.png') #이미지 경로로부터 불러오기 

##image=cv2.resize(image, dsize=(350,600),interpolation=cv2.INTER_LINEAR) #자꾸 오류떠서 그냥 화면 크기 맞춰주기(사진한정)

##

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/pi/Desktop/cctv/trainer/trainer2.yml')

font = cv2.FONT_HERSHEY_SIMPLEX

id=0

names = ['None', 'loze', 'YangDa99', 'minjung', 'minjung']

#image = cv2.imread('/home/pi/Desktop/cctv/test.png')


#while True:

#for (x,y,w,h) in body:
#while(True) :
while cv2.waitKey(27) < 0:
#이런것들이 없어야 카메라가 열린다.
    ret, image = cam.read()

    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #그레이 색상으로 화면 바꿔주기 (인식용.)
    
    #body = body_cascade.detectMultiScale(grayImage, scaleFactor = 1.2, minNeighbors = 5, minSize = (int(minW), int(minH)),) ##여기가 제일 문제많이 생김 
    body = body_cascade.detectMultiScale(grayImage, 1.03,5)
    face = face_cascade.detectMultiScale(grayImage, 1.03,5)
    
    
    
        #faces_in_body = face_cascade.detectMultiScale(body_image_gray, 1.03,5)

        
    for (fx,fy,fw,fh) in face:
            
        if (cv2.rectangle(image,(fx,fy),(fx+fw,fy+fh),(0,255,255),2)).any() :#얼굴을 인식했는가?
            
            cv2.rectangle(image,(fx,fy),(fx+fw,fy+fh),(0,255,255),2)
            
            id, confidence = recognizer.predict(grayImage[fy:fy+fh,fx:fx+fw]) ##여기가 제일 문제많이 생김 
            
            
            if (100-confidence  >= 10):

                id = names[id] #사람의 이름 그니까 

                confidence = "  {0}%".format(round(100 - confidence)) #만약 정확도가 100이하라면 100에서 정확도를 뺴서 인식도를 나타내라
            
                cv2.putText(image, str(id), (fx+5,fy-5), font, 1, (255,255,255), 2) #사람이름 이름 출력 

                cv2.putText(image, str(confidence), (fx+5,fy+fh-5), font, 1, (255,255,0), 1)  #정확도 퍼센트 출력
                
                #break
        
            
            
            elif (100-confidence < 10) : #내가 찾는 사람이 아니다 
                    
                
            
                #face_img = image[y:y+h, x:x+w] # 인식된 얼굴 이미지 crop

                #face_img = cv2.resize(image, dsize=(0, 0), fx=0.04, fy=0.04) # 축소

                #face_img = cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA) # 확대
        
                #image[y:y+h, x:x+w] = image
                  
                
                
                
                for (x,y,w,h) in body:
                    
                    if (cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),3)).any() :
    
                        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),3)
        
                        #body_image_gray = grayImage[y:y+h, x:x+w]

                        #body_image_color = image[y:y+h, x:x+w]
                        
                        t=cv2.resize(mozaic, dsize=(w,h), interpolation=cv2.INTER_LINEAR)
                
                        image[y:y+h, x:x+w] = t
        

 

#plt.figure(figsize=(12,12))
#plt.imshow('camera',image)
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()



    cv2.imshow('camera',image) #화면출력 

#cv2.waitKey(0) #얘로인해서 화면이 안나올 일은 없음 
cv2.destroyAllWindows()#누르면 꺼짐 

cam.release() 



