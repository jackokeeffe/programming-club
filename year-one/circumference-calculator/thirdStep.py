#Step Three: Advanced (Different Measurement Types)
import random

def ciDi(type, measurement, unit):
	if type == "ci":
		circumference = measurement
		diameter = measurement/3.14
		radius = diameter/2
		area = 3.14*(radius**2)

	elif type == "di":
		circumference = 3.14 * measurement
		diameter = measurement
		radius = measurement/2
		area = 3.14*(radius**2)

	print("circumference: " + str(circumference) + " " + unit)
	print("Diameter: " + str(diameter) + " " + str(unit))
	print("Radius: " + str(radius) + " " + unit)
	print("Area: " + str(area) + " " + unit)

ciDi("di", random.choice(range(1,10)), "cm")