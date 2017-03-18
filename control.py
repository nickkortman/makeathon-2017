#setup
stopped = True
at_destination = False

#control loop
while not at_destination:
    if stopped:
        #handle stopped
    
    elif:
        if at_intersection or not is_aligned or is_blocked:
            stop()

        #update position 
#done

def at_intersection():
    #read color sensor

def is_aligned():
    #check side ultrasonic

def is_blocked():
    #check front ultrasonic

def stop():
    #set motors to 0
    stopped = True

def left90():
    stopped = False
    #set right full ahead
    #set left full behind
    #wait certain amount of time
    stop()

def right90():
    stopped = False
    #set left full ahead
    #set right full behind
    #wait
    stop()

def turn_around():
    right90()
    right90()

def forward():
    stopped = False
    #set right and left full ahead

def left_turn():
    forward()
    #wait/use intersection sensor
    left90()
    forward()
    #wait/use intersection sensor
    stop()

def right_turn():
    forward()
    #wait/use intersection sensor
    right90()
    forward()
    #wait/use intersection sensor
    stop()