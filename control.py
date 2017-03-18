from motor import *

def at_intersection():
    #read color sensor

def is_aligned():
    #check side ultrasonic

def is_blocked():
    #check front ultrasonic

def stop(stepper):
    stepper.rotateBoth(0,0)
    stopped = True

def left90(stepper):
    stopped = False
    #change degrees to correct value
    stepper.rotateBoth(-360, 25)
    stop(stepper)

def right90(stepper):
    stopped = False
    #change degrees to correct value
    stepper.rotateBoth(360, 25)
    stop(stepper)

def turn_around(stepper):
    right90(stepper)
    right90(stepper)

def forward(stepper):
    stopped = False
    stepper.rotateBothOpp(10, 25)

def left_turn(stepper):
    forward(stepper)
    #wait/use intersection sensor
    left90(stepper)
    forward(stepper)
    #wait/use intersection sensor
    stop(stepper)

def right_turn(stepper):
    forward(stepper)
    #wait/use intersection sensor
    right90(stepper)
    straight_intersection(stepper)

def straight_intersection(stepper):
    while(not at_intersection):
        forward(stepper)
    straight_intersection(stepper)