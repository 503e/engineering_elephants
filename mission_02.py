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
robot.straight(distance=1400, then=Stop.HOLD)
robot.arc(radius=-150, angle=70, wait=True)
robot.straight(distance=305, then=Stop.HOLD, wait=True)
robot.arc(radius=-65, angle=75, wait=True)
robot.straight(distance=40, then=Stop.HOLD, wait=True)
robot.arc(radius=-65, angle=75, wait=True)
robot.turn(-90)
robot.arc(70, 90)