import os
import cv2
import numpy as np
from PIL import Image
import pickle
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

config = {
    "apiKey": "AIzaSyBQfdgpQTKl0i6j_tAJT0PHs2tmeeerDXs",
    "authDomain": "myguard-5b137.firebaseapp.com",
    "databaseURL": "https://myguard.australia-southeast1.firebasedatabase.app",
    "projectId": "myguard-5b137",
    "storageBucket": "myguard-5b137.appspot.com",
    "messagingSenderId": "908911774625",
    "appId": "1:908911774625:web:8b74fb448a9d8c1ae599e0",
    "measurementId": "G-884BC48JTH"
}



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "people")

face_cascade = cv2.CascadeClassifier("./cascades/data/haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_labels = []
x_train = []


'''Load DB configuration'''
# Use a service account
cred = credentials.Certificate('./myguard-5b137-firebase-adminsdk-4dwek-721bb997a7.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# result = db.collection('user').document("1").get()

# docs = db.collection(u'user').stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')


def load_img(role, email):
    docs = db.collection('user').where("role","==",role).where("email", "==", email).get()

    if len(docs) > 1 :
        return "ERROR"

    doc = docs[0].to_dict()
    img_url = doc["imgURL"]
    return img_url



def train_all_img():
    docs = db.collection('user').where("role","==","user").get()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
# if result.exists:
#     print(result.to_dict())

# for item in storage:
#     print(item)

# path_on_cloud = 
img_arr = load_img("user", "admin@gmail.com")

for url in img_arr:
    print(storage.child(url).get_url(None))



# for root, dirs, files in os.walk(image_dir):
#     for file in files:
#         if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
#             path = os.path.join(root, file)
#             label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
# 
#             # print(label, path)
#             if not label in label_ids:
#                 label_ids[label] = current_id
#                 current_id +=1
#             id_ = label_ids[label]
#             print(label_ids)
# 
#             pil_image = Image.open(path).convert("L") # greyScale
#             # size = (550, 550)
#             # final_image = pil_image.resize(size, Image.ANTIALIAS)
#             image_array = np.array(pil_image, "uint8")
#             # print(image_array)
# 
#             # Detect the faces using img-array
#             faces = face_cascade.detectMultiScale(image_array)
# 
#             # Store the faces
#             for (x,y,w,h) in faces:
#                 roi = image_array[y:y+h, x:x+w]
#                 x_train.append(roi)
#                 y_labels.append(id_)
# 
# Train the faces        
# with open("labels.pickle", 'wb') as f:
#     pickle.dump(label_ids, f)
# 
# recognizer.train(x_train, np.array(y_labels))
# recognizer.save("trainner.yml")