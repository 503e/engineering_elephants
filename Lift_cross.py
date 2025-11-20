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
robot.use_gyro(True)
main_motor.run_angle(600, -720, then=Stop.HOLD, wait=False)#move attachment down
robot.straight(distance=-480, then=Stop.HOLD,)
robot.turn(angle=-90, wait=True)
robot.straight(distance=-100, then=Stop.HOLD)
main_motor.run_angle(600, 400, then=Stop.HOLD, wait=True)
robot.turn(angle=90, wait=True)
main_motor.run_angle(600, -400, then=Stop.HOLD, wait=False)
wait(250)
robot.straight(distance=-160, then=Stop.HOLD,)
main_motor.run_angle(600, 720, then=Stop.HOLD, wait=True)
robot.turn(angle=130, wait=True)
robot.straight(distance=-350, then=Stop.HOLD,)
main_motor.run_angle(600, -800, then=Stop.HOLD, wait=True)
robot.straight(distance=200, then=Stop.HOLD,)
main_motor.run_angle(600, -100, then=Stop.HOLD, wait=False)
robot.turn(angle=-57, wait=True)
robot.straight(distance=-270, wait=True)
main_motor.run_angle(600, 700, then=Stop.HOLD, wait=True)#Minecart lift
main_motor.run_angle(600, -1200, then=Stop.HOLD, wait=False)
robot.turn(angle=75, wait=True)
robot.straight(distance=-225, wait=True)
main_motor.run_angle(600, 300, then=Stop.HOLD)
robot.turn(angle=-25, wait=True)
robot.straight(distance=100, wait=True)
robot.turn(angle=-45, wait=True)
robot.straight(distance=-600, wait=True)
robot.arc(radius=-500, angle=-95)
robot.straight(distance=-200)







