# 01/26/21: Mini Activity (Circumference Calculator)
#Inspiration: https://www.omnicalculator.com/math/circumference
#Step one: Basic Conversion (Circumference)

def circumference(measurement, unit):
	#Finding Values
	circumference = measurement
	diameter = measurement / 3.14
	radius = diameter / 2
	area = 3.14 * (radius ** 2)

	#Printing (in understandable way)
	print("circumference: " + str(circumference) + " " + unit)
	print("Diameter: " + str(diameter) + " " + unit)
	print("Radius: " + str(radius) + " " + unit)
	print("Area: " + str(area) + " " + unit)

if __name__ == '__main__':
	circumference(3, "cm")
