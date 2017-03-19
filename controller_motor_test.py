from bbio import run
from motor import *
import Adafruit_BBIO.GPIO as gpio
import numpy as np
import time
import datetime

LEFT_THROTTLE_PIN = "P9_14"
RIGHT_THROTTLE_PIN = "P9_16"

MOVING_AVERAGE_AMOUNT = 5 # Higher values means longer ramp time to get to max speed
DEADBAND_THRESHOLD = 0.5 # Higher values means less drift, but too high will limit variability in speed
HIGH_PW = 2000
LOW_PW = 1000
AVERAGE_PW = 1500
NORM_PW = 400.0

def micros():
    now = datetime.datetime.now()
    return now.microsecond

def pulseIn(gpio_pin, value, timeout=23200):
    endSig = value
    startSig = gpio.LOW if value==gpio.HIGH else gpio.HIGH
    
    start = micros()
    while gpio.input(gpio_pin) == startSig and (micros()-start) < timeout:
        if micros()-start > timeout:
            return timeout
    
    start = micros()
    while gpio.input(gpio_pin) == endSig and (micros()-start) < timeout:
        if micros()-start > timeout:
            return timeout
    
    return micros() - start

"""
Filter out very low controller inputs to prevent drift
"""
def deadband(value):
    if np.abs(value) < DEADBAND_THRESHOLD:
        return 0.0
    else:
        return value

"""
Tracks controller RC input with normalizing output between -1 and 1 with deadband
"""
def controllerInput(pin, avg):
    pw = pulseIn(pin, gpio.HIGH)
    if pw >= LOW_PW and pw <= HIGH_PW:
        avg = (avg / MOVING_AVERAGE_AMOUNT * (MOVING_AVERAGE_AMOUNT - 1) + pw / MOVING_AVERAGE_AMOUNT)
    norm = (avg - AVERAGE_PW) / NORM_PW
    
    if (norm > 1.0):
        norm = 1.0
    elif (norm < -1.0):
        norm = -1.0 
    return avg, deadband(norm)

def setup():
    gpio.setup(LEFT_THROTTLE_PIN, gpio.IN)
    gpio.setup(RIGHT_THROTTLE_PIN, gpio.IN)
    
def loop():
    avg_left = 0.0
    avg_right = 0.0
    
    stepper = Stepper()
    
    while True:
        avg_left, controller_out_left = controllerInput(LEFT_THROTTLE_PIN, avg_left)
        avg_right, controller_out_right = controllerInput(RIGHT_THROTTLE_PIN, avg_right)
        
        print(controller_out_left)
        print(controller_out_right)
        
        stepper.rotateLeft(10, 25)
        
        #if (np.abs(controller_out_left) > DEADBAND_THRESHOLD and np.abs(controller_out_right) > DEADBAND_THRESHOLD):
            #stepper.rotateLeft(10, 25)
            #stepper.rotateRight(10, 25)
        
        time.sleep(0.1)
       
# Start code
run(setup, loop)