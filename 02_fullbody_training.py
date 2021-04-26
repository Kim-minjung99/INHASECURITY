# -*- coding: utf-8 -*-
#카메라로 촬영한 30장의 사진을 학습시켜주는 기능을 한다. 
import cv2

import numpy as np

from PIL import Image

import os



# Path for face image database

path = 'trainervideo'

recognizer = cv2.body.LBPHFaceRecognizer_create()

detector = cv2.CascadeClassifier("/home/pi/Desktop/cctv/opencv-master/data/haarcascades/haarcascade_fullbody.xml");



# function to get the images and label data

def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     

    faceSamples=[]

    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale

        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])

        boides = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in boides:

            faceSamples.append(img_numpy[y:y+h,x:x+w])

            ids.append(id)

    return faceSamples,ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")

boides,ids = getImagesAndLabels(path)

recognizer.train(boides, np.array(ids))



# Save the model into trainer/trainer.yml

recognizer.write('trainer/trainer2.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces trained and end program

print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


