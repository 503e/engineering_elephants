from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.iodevices import XboxController

prime_hub = PrimeHub()
left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
main_motor = Motor(Port.F, Direction.CLOCKWISE)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

robot.use_gyro(True)

robot.straight(distance=-350, wait=True)
main_motor.run_angle(600, -800, then=Stop.HOLD, wait=True)
main_motor.run_until_stalled(-10000, then=Stop.COAST, duty_limit=15)
robot.straight(distance=100, wait=True)
robot.turn(-90, wait=True)
robot.straight(distance=-50, wait=True)
robot.arc(radius=-100, angle=-90, wait=True)
robot.straight(distance=-250, wait=True)
robot.straight(distance=150, wait=True)
robot.turn(-150, wait=True) #Com# pletion of  Ship Raise and aligned for mission "map reveal"
robot.arc(radius=500, angle=-75, wait=True)