from motor import *
auton = False
destination = False
stepper = Stepper()
#-1 = left, 0 = straight, 1 = right
directions = [1, 0, -1, 0]

def manual_mode:
	# Get controller output
	# TODO: Do somefin' here
	
	# Set wheel speeds
	# TODO: Do somefin' here
	pass

def autonomous_mode:
	while(not destination):
		if(at_intersection):
			time.sleep(2)
			dir = directions[0]
			if(dir == -1):
				left_turn()
			elif(dir == 0):
				straight_intersection()
			else:
				right_turn()
			if(len(directions) == 1):
				#drive forward enough
				destination = true
			else:
				directions = directions[1:]
		else:
			forward()
	pass

def setup:
	# Generate the map
	# TODO: Do somefin' here
	
	# Start A* algorithm
	# TODO: Do somefin' here
	pass

def loop:
	while (True):
	
		# Check if we're in auton or manual mode
		# TODO: Do somefin' here
	
		if (not auton):
			manual_mode()
		else:
			autonomous_mode()
			
		# Prevents case when nothing is run, so code doesn't run too fast
		time.sleep(0.1)

run(setup, loop)

from motor import *

def at_intersection():
    #read color sensor

def is_aligned():
    #check side ultrasonic

def is_blocked():
    #check front ultrasonic

def stop():
    stepper.rotateBoth(0,0)
    stopped = True

def left90():
    stopped = False
    #change degrees to correct value
    stepper.rotateBoth(-360, 25)
    stop()

def right90():
    stopped = False
    #change degrees to correct value
    stepper.rotateBoth(360, 25)
    stop()

def turn_around():
    right90()
    right90()

def forward():
    stopped = False
    stepper.rotateBothOpp(10, 25)

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
    straight_intersection()

def straight_intersection():
    while(not at_intersection):
        forward()
    straight_intersection()