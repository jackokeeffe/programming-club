#Extra Step: Advanced (More Types, sqrt())
import math
import random

def ciDiRaAr(type, measurement, unit):
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

	elif type == "ra":
		circumference = 3.14*(measurement*2)
		diameter = measurement*2
		radius = measurement
		area = 3.14*(measurement**2)

	elif type == "ar":
		area = measurement
		radius = math.sqrt(measurement/math.pi)
		diameter = radius*2
		circumference = 3.14*diameter

	print("circumference: " + str(circumference) + " " + unit)
	print("Diameter: " + str(diameter) + " " + unit)
	print("Radius: " + str(radius) + " " + unit)
	print("Area: " + str(area) + " " + unit)

random_number = random.randint(1,10)
print(random_number)
ciDiRaAr("ra", random_number, "cm")

#Pi Function in Math Library
print(math.pi)
