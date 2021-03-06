# -*- coding: utf-8 -*-
import numpy as np
import cv2
import picamera
import os
import datetime
    
savepath = '/home/pi/Desktop/cctv/savepath' #동영상저장경로
def record():
        with picamera.PiCamera() as camera:
            camera.resolution = (640,480)
            now = datetime.datetime.now()
            filename = now.strftime('%Y-%m-%d_%H:%M:%S')
            camera.start_recording(output = savepath + '/' + filename +'.h264')
            camera.wait_recording(60)
            camera.stop_recording()

while True:
    record() #cctv역할로 카메라 촬영 기능 구동. 10초에 한번씩 동영상 촬영. 지정된 경로로 지정된 파일명으로 저장 

    
camera.release()
cv2.destroyAllWindows()