import cv2
import os
import numpy as np
import sys
import pickle


face_cascade = cv2.CascadeClassifier("./cascades/data/haarcascade_frontalface_alt2.xml")
eye_cascade = cv2.CascadeClassifier("./cascades/data/haarcascade_eye.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {}
with open("labels.pickle", 'rb') as f:
    old_labels = pickle.load(f)
    # Reverse the original labels in pickle
    labels = {v:k for k,v in old_labels.items()}


while(True):

    # Capture fram-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x,y,w,h) in faces:
        # print(x,y,w,h)
        roi_gray = gray[y:y+h,x:x+w] 
        roi_color = frame[y:y+h,x:x+w]

        id_, conf = recognizer.predict(roi_gray)
        if conf>=45 and conf<=95:
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 4, color, stroke, cv2.LINE_AA)
        # img_item = "my-image.png"
        # cv2.imwrite(img_item, roi_gray)

        color = (255,0,0)
        stoke = 2
        end_x = x + w
        end_y = y + h
        cv2.rectangle(frame, (x,y), (end_x, end_y), color, stoke)

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), color, stoke)

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
