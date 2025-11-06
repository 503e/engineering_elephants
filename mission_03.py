from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.iodevices import XboxController

left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
main_motor = Motor(Port.F, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)
robot.settings(straight_speed=750,straight_acceleration=600, turn_rate=500, turn_acceleration=350)#adjusts the speed that the robot runs at
robot.use_gyro(True)
main_motor.run_angle(600, -1000, then=Stop.HOLD, wait=True)#move attachment down
robot.straight(distance=-700, then=Stop.HOLD, wait=True)
robot.turn(90, wait=True)
robot.straight(distance=-350, then=Stop.HOLD, wait=True)
robot.turn(-70, wait=True)
main_motor.run_angle(600, 900, then=Stop.HOLD, wait=True)#lift
robot.turn(67, wait=True)
robot.straight(distance=-800, then=Stop.HOLD, wait=True)
robot.arc(radius=-200, angle=-70, wait=True)
robot.straight(distance=-800, then=Stop.HOLD, wait=True)