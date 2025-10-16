from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color, Button
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.iodevices import XboxController

prime_hub = PrimeHub()
left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

robot.use_gyro(True)

# base speed in mm/s
base_speed = 100
# set robot speed to five times the base speed
robot.settings(straight_speed=base_speed * 5)

# drive straight for 200 mm at the configured speed
robot.straight(distance=200, wait=True)
robot.arc(500, angle=60, then=Stop.HOLD, wait=True)

turn_percent = 1.0
original_turn_angle = 65
turn_angle = int(original_turn_angle * turn_percent)
robot.turn(turn_angle, then=Stop.HOLD, wait=True)
robot.straight(distance=1000, wait=True)
turn_percent = 1.0
original_turn_angle = -80
turn_angle = int(original_turn_angle * turn_percent)
robot.turn(turn_angle, then=Stop.HOLD, wait=True)
robot.arc(250, angle=180, then=Stop.HOLD, wait=True)
turn_percent = 1.0
original_turn_angle = -90
turn_angle = int(original_turn_angle * turn_percent)
robot.turn(turn_angle, then=Stop.HOLD, wait=True)