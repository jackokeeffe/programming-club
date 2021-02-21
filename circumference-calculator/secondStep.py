from firstStep import circumference

#Step Two: Using Random Library (introduction for next week)
import random
random_measurement = random.randint(1, 10)
print("Random measurement: " + str(random_measurement) + "cm")
circumference(random_measurement, "cm")