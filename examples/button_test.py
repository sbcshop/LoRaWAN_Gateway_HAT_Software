#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import time
import RPi.GPIO as GPIO

KEY1_PIN = 17
KEY2_PIN = 27

GPIO.setmode(GPIO.BCM) 
GPIO.setup(KEY1_PIN,GPIO.IN) # Input with pull-up
GPIO.setup(KEY2_PIN,GPIO.IN) # Input with pull-up

while True:
    if GPIO.input(KEY1_PIN) == GPIO.LOW: # button is released
        print("button 1")

    if GPIO.input(KEY2_PIN) == GPIO.LOW: # button is released
        print("button 2")

    time.sleep(0.2)




 
        
