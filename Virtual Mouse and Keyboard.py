import cv2
import mediapipe as mp
import math
import time
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    cv2.imshow('Virtual Mouse',frame)
    cv2.waitKey(1)
