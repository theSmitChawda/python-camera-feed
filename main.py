# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:15:15 2022

@author: Administrator
"""

import numpy as np
import cv2 as cv

#!wget --no-check-certificate -O 420-08.jpg https://cdn-shop.adafruit.com/1200x900/420-08.jpg

import cv2 as cv
cap = cv.VideoCapture(0)
ret=True
while True:
    ret, frame = cap.read()
    cv.namedWindow('test_frame',cv.WINDOW_NORMAL)
    cv.imshow('test_frame',frame)
    if cv.waitKey(1) & 0xFF == 27:
        break
        
cap.release()
cv.destroyAllWindows()