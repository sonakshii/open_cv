import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 3 )
    for (x, y, w, h ) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h),(255, 0, 0), 2)
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 18)
    for (p, q, r, s) in eyes:
        cv2.rectangle(img, (p ,q), (p+r, q+s),(0, 255, 0), 1)
    smiles = smile_cascade.detectMultiScale(gray, 1.8, 15)
    for (p, q, r, s) in smiles:
        cv2.rectangle(img, (p ,q), (p+r, q+s),(0, 0,255), 1)
    cv2.imshow('img', img)
    k=cv2.waitKey(30)& 0xff
    if k==27:
        break
cap.release()