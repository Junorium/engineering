# ENGR010
# Lab4
# JR Perez
# jrp527

from gpiozero import CamJamKitRobot
from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=17)
robot = CamJamKitRobot()
ratio = 1.2
# all functions must have the three parameters:
# percentage of maximum speed
# duration in seconds 
# direction

# 90 deg is 0.55 sec at 100%
# 180 deg is 1.10 sec at 100%
# possible args for direction: forward, backward, stop
def linear(speed, ratio, duration, direction):
  if direction == 'forward':
    robot.value = (speed * ratio, speed)
    sleep(duration)
  elif direction == 'backward':
    robot.value = (-speed * ratio, -speed)
    sleep(duration)
  elif direction == 'stop':
    robot.value = (0, 0)
    sleep(duration)

# possible args for direction: left, right
def turn(speed, ratio, duration, direction):
  if direction == 'left':
    robot.value = (0, speed)
    sleep(duration)
  elif direction == 'right':
    robot.value = (speed * ratio, 0)
    sleep(duration)

# possible args for direction: clockwise, counterclockwise
def rotate(speed, ratio, duration, direction):
  if direction == 'cw' or direction == 'clockwise':
    robot.value = (speed * ratio, -speed)
    sleep(duration)
  elif direction == 'ccw' or direction == 'counterclockwise':
    robot.value = (-speed * ratio, speed)
    sleep(duration)

try:
        while True:
                distance = sensor.distance * 100

                if 10 <= distance:
                        print(f'Distance: {distance}cm')
                        linear(0.5, ratio, 0.5, 'forward')

                if distance < 10:
                        print('Linear movement: L: -0.68, R: -0.75 for 1000ms, Backward')
                        linear(0.75, ratio, 1, 'backward')

                        print('Rotate: L: -0.9, R: 1 for 1000ms, Counter-clockwise')
                        rotate(0.75, ratio, 1, 'counterclockwise')

                        print('Linear movement: L: 0.45, R: 0.5 for 1000ms, Forward')
                        linear(0.5, ratio, 1, 'forward')

                        print('Rotate: L: 0.9, R: -1 for 1000ms, Clockwise')
                        rotate(0.75, ratio, 1, 'clockwise')

                        print('Linear movement: L: 0.45, R: 0.5 for 1000ms, Forward')
                        linear(0.5, ratio, 2, 'forward')

                        print('Rotate: L: 0.9, R: -1 for 1000ms, Clockwise')
                        rotate(0.75, ratio, 1, 'clockwise')

                        print('Linear movement: L: 0.45, R: 0.5 for 1000ms, Forward')
                        linear(0.5, ratio, 1, 'forward')
except KeyboardInterrupt:
        quit()
