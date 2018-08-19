import os
import cv2
import numpy as np
import pickle
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

x_train = []
y_labels = []

current_id = 0
label_ids = {}

# Loading images
image_dir = os.path.join(BASE_DIR, "images")

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith('png') or file.endswith('jpg'):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(' ', '_').lower()
            # print(label, path)

            if label in label_ids:
                pass
            else:
                label_ids[label] = current_id
                current_id += 1

            id_ = label_ids[label]
            # print(label_ids)
            pil_image = Image.open(path).convert('L')  # grayscale
            image_array = np.array(pil_image, 'uint8')
            # print(image_array)

            # Detecting Face's Region of Interest
            # and append it to training set with it's corresponding label in y_labels
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
            for x, y, w, h in faces:
                roi = image_array[y:y + h, x:x + w]
                x_train.append(roi)
                y_labels.append(id_)

# print(y_labels)
# print(x_train)

# Using Pickle to Save Label IDs
with open('labels.pickle', 'wb') as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("recognizers/face-trainer.yml")
