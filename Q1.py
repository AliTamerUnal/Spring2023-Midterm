


#############################
# Add your code before here

def Run():
	x = AirlinesInTurkey()
	a = x.add_airline("THY")
	a.add_aircraft(BOEING(11)) 
	a.add_aircraft(AIRBUS(22)) 
	a.add_aircraft(BOEING(33))

	a = x.add_airline("Pegasus")
	a.add_aircraft(BOEING(101)) 
	a.add_aircraft(BOEING(102)) 
	a.add_aircraft(BOEING(103))

	return x.report()
