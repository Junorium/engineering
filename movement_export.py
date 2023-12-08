# ENGR010
# Lab5
# JR Perez
# jrp527

from gpiozero import CamJamKitRobot
from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=17)
robot = CamJamKitRobot()
ratio = 1.0

def write(time):
    for i in range(int(time * 10)):
        distance_file.write(f'{distance}\n')
        print(distance)
        sleep(0.1)
                                
def linear(speed, ratio, duration, direction):
  if direction == 'forward':
    robot.value = (speed * ratio, speed)
    write(duration)
  elif direction == 'backward':
    robot.value = (-speed * ratio, -speed)
    write(duration)
  elif direction == 'stop':
    robot.value = (0, 0)
    write(duration)

# possible args for direction: left, right
def turn(speed, ratio, duration, direction):
  if direction == 'left':
    robot.value = (0, speed)
    write(duration)
  elif direction == 'right':
    robot.value = (speed * ratio, 0)
    write(duration)

# possible args for direction: clockwise, counterclockwise
def rotate(speed, ratio, duration, direction):
  if direction == 'cw' or direction == 'clockwise':
    robot.value = (speed * ratio, -speed)
    write(duration)
  elif direction == 'ccw' or direction == 'counterclockwise':
    robot.value = (-speed * ratio, speed)
    write(duration)

try:
        while True:
                distance = sensor.distance * 100
                with open('distance_data.txt', 'w') as distance_file:
                    with open('movement_data.txt','w') as movement_file:
                        

                        linear(1, ratio, 2, 'forward')
                        movement_file.write("Linear\n1\n1\n2000\nForward\n" * 2)
                        write(0.6)
                              
                        turn(1, ratio, 1, 'left')
                        movement_file.write("Turn\n0\n1\n1000\nLeft\n" * 10)
                        write(0.6)
                              
                        linear(0.75, ratio, 2, 'forward')
                        movement_file.write("Linear\n0.75\n0.75\n2000\nForward\n" * 20)
                        write(1)
                              
                        rotate(1, ratio, 0.5, 'clockwise')
                        movement_file.write("Rotate\n1\n-1\n500\nClockwise\n" * 5)
                        write(2)

                        linear(0.5, ratio, 2, 'forward')
                        movement_file.write("Linear\n0.5\n0.5\n2000\nForward\n" * 20)
                        write(0.5)

                        turn(1, ratio, 1, 'right')
                        movement_file.write("Turn\n1\n0\n1000\nRight\n" * 10)
                        write(0.3)

                        linear(0.75, ratio, 2, 'backward')
                        movement_file.write("Linear\n0.75\n0.75\n2000\nBackward\n" * 20)
                        write(0.4)

                        quit()
except KeyboardInterrupt:
        quit()
