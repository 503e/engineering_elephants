from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)
robot.use_gyro(True)
robot.straight(distance=730, then=Stop.HOLD, wait=True)
robot.arc(radius=-100, angle=95, wait=True)
robot.turn(-90, wait=True)
robot.straight(distance=100, then=Stop.HOLD, wait=True)
robot.arc(radius=240, angle=55, wait=True)
robot.straight(distance=225, then=Stop.HOLD, wait=True)
robot.arc(radius=280, angle=190, wait=True)
robot.turn(70, wait=True)
robot.straight(distance=210, then=Stop.HOLD, wait=True)
