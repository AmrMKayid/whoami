import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizers/face-trainer.yml")

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for x, y, w, h in faces:
        # print(x, y, w, h)
        # Region of Interest
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Recognizer
        id_, conf = recognizer.predict(roi_gray)
        if 45 <= conf <= 85:
            print(id_)

        # img_item = 'my_img.png'
        # cv2.imwrite(img_item, roi_color)

        color = (255, 0, 0)  # BGR
        stroke = 2  # how thick the line should be
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
