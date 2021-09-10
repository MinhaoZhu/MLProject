import cv2
import os
import numpy as np
import sys
import pickle


face_cascade = cv2.CascadeClassifier("cascades/data/haarcascade_frontalface_alt2.xml")

# Read the input image

img = cv2.imread('imgs/happy/0-4.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 4)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()