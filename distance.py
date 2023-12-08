# ENGR010
# Lab 4
# JR Perez
# jrp527

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo = 18, trigger = 17)
try:
	while True:
		distance = sensor.distance * 100
		if 10 <= distance <= 20:
			print(f'Distance: {distance}cm')
		else:
			continue
except KeyboardInterrupt:
	quit()
