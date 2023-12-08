# ENGR010
# Lab 6
# JR Perez
# jrp527
import csv
from gpiozero import CamJamKitRobot
from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=17)
robot = CamJamKitRobot()

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

def stop(speed, ratio, duration, direction):
  robot.value = (0,0)
  sleep(duration)

try:
  with open('move_commands.csv', newline='') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
      param1, param2, param3, param4, param5 = row
      param2 = int(param2)
      param3 = int(param3)
      param4 = int(param4)
      if param1 == None:
        pass
      elif param1 == "linear":
        linear(param2, param3, param4, param5)
      elif param1 == "turn":
        turn(param2, param3, param4, param5)
      elif param1 == "rotate":
        rotate(param2, param3, param4, param5)
      elif param1 == "stop":
        stop(param2, param3, param4, param5)
      
except KeyboardInterrupt:
        quit()
