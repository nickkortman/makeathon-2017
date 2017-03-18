auton = False


def manual_mode:
	# Get controller output
	# TODO: Do somefin' here
	
	# Set wheel speeds
	# TODO: Do somefin' here
	pass

def autonomous_mode:
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