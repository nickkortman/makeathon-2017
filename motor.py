from __future__ import division
import Adafruit_BBIO.GPIO as GPIO
import time
import math


def initialize_pins(pins):
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

def set_all_pins_low(pins):
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
        
def wavedrive(pins, pin_index):
    for i in range(len(pins)):
        if i == pin_index:
            GPIO.output(pins[i], GPIO.HIGH)
        else:
            GPIO.output(pins[i], GPIO.LOW)

def fullstep(pins, pin_index):
    """pin_index is the lead pin"""
    GPIO.output(pins[pin_index], GPIO.HIGH)
    GPIO.output(pins[(pin_index+3) % 4], GPIO.HIGH)
    GPIO.output(pins[(pin_index+1) % 4], GPIO.LOW)
    GPIO.output(pins[(pin_index+2) % 4], GPIO.LOW)


class Stepper(object):
    def __init__(self, steps_per_rev=2048.0,
                 rightPins=["P8_7", "P8_9", "P8_11", "P8_15"],
                 leftPins=["P8_8", "P8_10", "P8_12", "P8_14"]):

        self.leftPins = leftPins
        self.rightPins = rightPins
        
        initialize_pins(self.leftPins)
        set_all_pins_low(self.leftPins)
        initialize_pins(self.rightPins)
        set_all_pins_low(self.rightPins)
        
        self.leftAngle = 0
        self.rightAngle = 0
        self.steps_per_rev = steps_per_rev
        
        # Initialize stepping mode
        self.drivemode = fullstep
    
    def rotateBoth(self, degrees, rpm=15):
        step = 0
        
        # Calculate time between steps in seconds
        wait_time = 60.0/(self.steps_per_rev*rpm)
        
        # Convert degrees to steps
        steps = math.fabs(degrees*self.steps_per_rev/360.0)
        self.rightDirection = 1
        self.leftDirection = 1
        
        if degrees < 0:
            self.leftPins.reverse()
            self.rightPins.reverse()
            self.rightDirection = -1
            self.leftDirection = -1
        
        while step < steps:
            for pin_index in range(len(self.leftPins)):
                self.drivemode(self.leftPins, pin_index)
                self.drivemode(self.rightPins, pin_index)
                time.sleep(wait_time)
                step += 1
                self.leftAngle = (self.leftAngle + self.leftDirection/self.steps_per_rev \
                *360.0) % 360.0
                self.rightAngle = (self.rightAngle + self.rightDirection/self.steps_per_rev \
                *360.0) % 360.0
        
        if degrees < 0:
            self.leftPins.reverse()
            self.rightPins.reverse()
        
        set_all_pins_low(self.leftPins)
        set_all_pins_low(self.rightPins)

    #degrees are left degrees, right is opposite direction, use negative if you want positive right
    def rotateBothOpp(self, degrees, rpm=15):
        step = 0
        
        # Calculate time between steps in seconds
        wait_time = 60.0/(self.steps_per_rev*rpm)
        
        # Convert degrees to steps
        steps = math.fabs(degrees*self.steps_per_rev/360.0)
        self.rightPins.reverse()
        self.rightDirection = -1
        self.leftDirection = 1
        
        if degrees < 0:
            self.leftPins.reverse()
            self.rightPins.reverse()
            self.rightDirection = 1
            self.leftDirection = -1
        
        while step < steps:
            for pin_index in range(len(self.leftPins)):
                self.drivemode(self.leftPins, pin_index)
                self.drivemode(self.rightPins, pin_index)
                time.sleep(wait_time)
                step += 1
                self.leftAngle = (self.leftAngle + self.leftDirection/self.steps_per_rev \
                *360.0) % 360.0
                self.rightAngle = (self.rightAngle + self.rightDirection/self.steps_per_rev \
                *360.0) % 360.0
        
        if degrees < 0:
            self.leftPins.reverse()
            self.rightPins.reverse()
        
        set_all_pins_low(self.leftPins)
        set_all_pins_low(self.rightPins)
        
    def rotateLeft(self, degrees, rpm=15):
        step = 0
        
        # Calculate time between steps in seconds
        wait_time = 60.0/(self.steps_per_rev*rpm)
        
        # Convert degrees to steps
        steps = math.fabs(degrees*self.steps_per_rev/360.0)
        self.leftDirection = 1
        
        if degrees < 0:
            self.leftPins.reverse()
            self.leftDirection = -1
        
        while step < steps:
            for pin_index in range(len(self.leftPins)):
                self.drivemode(self.leftPins, pin_index)
                time.sleep(wait_time)
                step += 1
                self.leftAngle = (self.leftAngle + self.leftDirection/self.steps_per_rev \
                *360.0) % 360.0
        
        if degrees < 0:
            self.leftPins.reverse()
        
        set_all_pins_low(self.leftPins)
        set_all_pins_low(self.rightPins)

    def rotateRight(self, degrees, rpm=15):
        step = 0
        
        # Calculate time between steps in seconds
        wait_time = 60.0/(self.steps_per_rev*rpm)
        
        # Convert degrees to steps
        steps = math.fabs(degrees*self.steps_per_rev/360.0)
        self.rightDirection = 1
        
        if degrees < 0:
            self.rightPins.reverse()
            self.rightDirection = -1
        
        while step < steps:
            for pin_index in range(len(self.rightPins)):
                self.drivemode(self.rightPins, pin_index)
                time.sleep(wait_time)
                step += 1
                self.rightAngle = (self.rightAngle + self.rightDirection/self.steps_per_rev \
                *360.0) % 360.0
        
        if degrees < 0:
            self.rightPins.reverse()
        
        set_all_pins_low(self.leftPins)
        set_all_pins_low(self.rightPins)

    def zero_angle(self):
        self.leftAngle = 0
        self.rightAngle = 0
        

# def main():
#     stepper = Stepper()
#     stepper.rotate(180, 10)

# if __name__ == "__main__":
#     main()