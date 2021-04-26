
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import picamera
import time




body_classifier = cv2.CascadeClassifier('/home/pi/Desktop/cctv/opencv-master/data/haarcascades/haarcascade_fullbody.xml') #body xml을 사용하겠다 명시 
# Initiate video capture for video file


with picamera.PiCamera() as camera:
    camera.resolution=(640,480)
    camera.start_recording(output='body.h264')
    camera.wait_recording(10)
    camera.stop_recording()
#카메라 촬영하기 body.h264이름으로 저장하기 10초동안 촬영 

cap = cv2.VideoCapture('/home/pi/Desktop/cctv/body.h264') #경로를 따라 사진 캡쳐 
# Loop once video is successfully loaded
while cap.isOpened():
    
    # Read first frame
    ret, frame = cap.read()
    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray, 1.1, 3)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Pedestrians', frame)
	
	if cv2.waitKey(1) == 27 :
		break

cap.release()
cv2.destroyAllWindows()
