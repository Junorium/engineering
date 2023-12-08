from gpiozero import CamJamKitRobot
from time import sleep

robot = CamJamKitRobot()

# all functions must have the three parameters:
# percentage of maximum speed
# duration in seconds 
# direction

# possible args for direction: forward, backward, stop
def linear(speed, duration, direction):
  if direction == 'forward' or direction:
    robot.forward(speed)
    sleep(duration)
  elif direction == 'backward':
    robot.backward(speed)
    sleep(duration)
  elif direction == 'stop':
    robot.stop()
    sleep(duration)

# possible args for direction: left, right
def turn(speed, duration, direction):
  if direction == 'left':
    robot.left(speed)
    sleep(duration)
  elif direction == 'right':
    robot.right(speed)
    sleep(duration)

# possible args for direction: clockwise, counterclockwise
def rotate(speed, duration, direction):
  if direction == 'cw' or direction == 'clockwise':
    robot.value(speed, -speed)
    sleep(duration)
  elif direction == 'ccw' or direction == 'counterclockwise':
    robot.value(-speed, speed)
    sleep(duration)
