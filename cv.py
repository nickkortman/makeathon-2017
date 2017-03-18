import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    lower_red = np.array([0,100,100])
    upper_red = np.array([10,255,255])
    lower_green = np.array([40,100,100])
    upper_green = np.array([80,255,255])

    # Threshold the HSV image to get only blue colors
    greenMask = cv2.inRange(hsv, lower_green, upper_green)
    redMask = cv2.inRange(hsv, lower_red, upper_red)
    # Bitwise-AND mask and original image
    greenRes = cv2.bitwise_and(frame,frame, mask= greenMask)
    redRes = cv2.bitwise_and(frame,frame, mask= redMask)
    greenAvg = np.average(np.average(greenRes, axis=0), axis=0)
    redAvg = np.average(np.average(redRes, axis=0), axis=0)
    if(greenAvg[1] > .5):
        print "green"
    elif(redAvg[2] > .5):
        print "red"
    else:
        print "no color"
    cv2.imshow('frame',frame)
    cv2.imshow('green',greenRes)
    cv2.imshow('red',redRes)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()