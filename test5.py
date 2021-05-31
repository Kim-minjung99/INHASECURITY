# -*- coding: utf-8 -*-
##이거는 카메라를 틀어서 진행시키는것 
import numpy as np
import cv2
import picamera
import os
os.environ['OPENCV_IO_MAX_IMAGE_PIXELS']=str(2**64)
import datetime
##샾 두개는 카메라를 키거나 영상 이용시 사용할 코드이다.

###얼굴이 인식되지 않고 바디가 인식되지 않으면 일단 블랙처리인거다 
###수정 : 얼굴이 인식은 계속적으로 된다. 근데.. 지금 얼굴 인식이 되고 있는데, 그안에서 누군지는 모르고(얼굴만 인식중) 바디가 모자이크 처리가 안될때는 블랙처리 해줘야겠지..

face_cascade = cv2.CascadeClassifier(r"/home/pi/Desktop/cctv/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(r"/home/pi/Desktop/cctv/opencv-master/data/haarcascades/haarcascade_fullbody.xml")

cam = cv2.VideoCapture('/home/pi/Desktop/cctv/savepath/2021-05-10 05:15:07.h264') #저장된 영상 재생
#cam = cv2.VideoCapture(0)

cam.set(3, 640) # set video widht
cam.set(4, 480)

mozaic=cv2.imread('/home/pi/Desktop/cctv/mozaic.png')
finding=cv2.imread('/home/pi/Desktop/cctv/사진/finding.png')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/pi/Desktop/cctv/trainer/trainer2.yml')

font = cv2.FONT_HERSHEY_SIMPLEX

id=0

names = ['None', 'loze', 'YangDa99', 'minjung', 'minjung'] #사람이름 하드코딩한것... 나중에 이름 받아와서 처리해야한다.




while cv2.waitKey(27) < 0:   #이런것들이 없어야 카메라가 열린다.
    
    ret, image = cam.read()

    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #그레이 색상으로 화면 바꿔주기 (인식용.)
    real_image = cv2.cvtColor(image, cv2.IMREAD_COLOR) #이미지를 디폴트 값인 컬러 이미지로 저장 
    
    #image = finding_image #블랙처리 이미지 
    
    body = body_cascade.detectMultiScale(grayImage, 1.03,5)
    face = face_cascade.detectMultiScale(grayImage, 1.03,5)
    
    #여기 밑으로 블랙처리 코드를 넣으면 먹질 않음... for문으로 이미지 받아들이는 형태가 달라서 그런가 
        
    for (fx,fy,fw,fh) in face:
            
        if (cv2.rectangle(image,(fx,fy),(fx+fw,fy+fh),(0,255,255),1)).any() :#얼굴을 인식했는가?
            
            real_image = cv2.resize(image, dsize=(640,480), interpolation=cv2.INTER_LINEAR) #실제 이미지 다시 불러오기
            
            print('face Detected')
            
            cv2.rectangle(image,(fx,fy),(fx+fw,fy+fh),(0,255,255),1)
            
            id, confidence = recognizer.predict(grayImage[fy:fy+fh,fx:fx+fw]) ##여기가 제일 문제많이 생김 
            
            if (100-confidence >= 10):
                
                #real_image = cv2.resize(image, dsize=(640,480), interpolation=cv2.INTER_LINEAR)
                
                #image = real_image

                id = names[id] #사람의 이름 그니까 

                confidence = "  {0}%".format(round(100 - confidence)) #만약 정확도가 100이하라면 100에서 정확도를 뺴서 인식도를 나타내라
            
                cv2.putText(image, str(id), (fx+5,fy-5), font, 1, (255,255,255), 2) #사람이름 이름 출력 

                cv2.putText(image, str(confidence), (fx+5,fy+fh-5), font, 1, (255,255,0), 1)  #정확도 퍼센트 출력
                
        
            
            
            elif (100-confidence < 10) :#내가 찾는 사람이 아니다
                
                for (x,y,w,h) in body:
                    
                    #real_image = cv2.resize(image, dsize=(640,480), interpolation=cv2.INTER_LINEAR)
                
                    #image = real_image
                    
                    if (cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),1)).any() :
                        
                        print('body Detected')
    
                        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),1)
        
                        #body_image_gray = grayImage[y:y+h, x:x+w]

                        #body_image_color = image[y:y+h, x:x+w]
                        
                        t=cv2.resize(mozaic, dsize=(w,h), interpolation=cv2.INTER_LINEAR)
                
                        image[y:y+h, x:x+w] = t
                        
                    else:
                        finding_image = cv2.resize(finding, dsize=(640, 480), interpolation=cv2.INTER_LINEAR)
                        image = finding_image
                
            else:#얼굴인식이 10%를 넘지도, 10%를 못넘기지도 못한다면 에러처리 
                print('detected ERROR')
                finding_image = cv2.resize(finding, dsize=(640, 480), interpolation=cv2.INTER_LINEAR)
                image = finding_image

            
        else: #만약 얼굴 rectangle을 그리지 못했다면?
            print('Faces are not detected')
            finding_image = cv2.resize(finding, dsize=(640, 480), interpolation=cv2.INTER_LINEAR) #블랙처리 이미지 선언
            image = finding_image
            


    cv2.imshow('camera',image) #화면출력 

#cv2.waitKey(0) #얘로인해서 화면이 안나올 일은 없음 
cv2.destroyAllWindows()#누르면 꺼짐 

cam.release() 




