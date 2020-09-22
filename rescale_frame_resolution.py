import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#TO CHANGE RESOLUTion
def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

#make_1080p()

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

#make_720p()

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

#make_480p()

def change_res(width, height):   #call change_res(x,y)
    cap.set(3, width)
    cap.set(4, height)

#TO rescale frame (SCALING FACTOR)
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # calling rescale_frame function
    frame = rescale_frame(frame, percent=30)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()