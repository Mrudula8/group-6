#!/usr/bin/python
import time
import RPi.GPIO as io
#from motor_function import MotorDirection

water_sensor = 26
io.setmode(io.BCM)
io.setup(water_sensor, io.IN)
try:
	if io.input(water_sensor):
		active_time = time.time()
		print("Not Raining")
		print(active_time)
		#MotorDirection(-1)

	else:
		active_time = time.time()
		print("It's Raining")
		print(active_time)
		#MotorDirection(1)

except KeyboardInterrupt:
	print "\nUser Halt!"
finally:
	io.cleanup()
