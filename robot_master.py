from control import *
auton = False

#-1 = left, 0 = straight, 1 = right
directions = [1, 0, -1, 0]

def manual_mode:
	# Get controller output
	# TODO: Do somefin' here
	
	# Set wheel speeds
	# TODO: Do somefin' here
	pass

def autonomous_mode:
	if(stopped):
		if(at_intersection):
			if(direction[0] = -1):
				turn_left()
			elif(direction[0] = 0):
				straight_intersection()
			else:
				turn_right()
			directions = directions[1:]
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
	
		if (auton):
			manual_mode()
		else:
			autonomous_mode()
			
		# Prevents case when nothing is run, so code doesn't run too fast
		time.sleep(0.1)

run(setup, loop)