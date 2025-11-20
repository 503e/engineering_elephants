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
main_motor.run_angle(600, -750, then=Stop.HOLD, wait=False)#move attachment down
robot.straight(distance=-460, then=Stop.HOLD,)#was 480
robot.turn(angle=-90, wait=True)
robot.straight(distance=-100, then=Stop.HOLD)
main_motor.run_angle(600, 400, then=Stop.HOLD, wait=True)
robot.turn(angle=90, wait=True)
main_motor.run_angle(600, -400, then=Stop.HOLD, wait=False)
wait(250)
robot.straight(distance=-180, then=Stop.HOLD,)#was 160
main_motor.run_angle(600, 720, then=Stop.HOLD, wait=True)
robot.turn(angle=130, wait=True)
robot.straight(distance=-385, then=Stop.HOLD,)
main_motor.run_angle(600, -900, then=Stop.HOLD, wait=True)
robot.straight(distance=200, then=Stop.HOLD,)
main_motor.run_angle(600, -100, then=Stop.HOLD, wait=False)
robot.turn(angle=-57, wait=True)
robot.straight(distance=-270, wait=True)
main_motor.run_angle(600, 800, then=Stop.HOLD, wait=True)#Minecart lift
main_motor.run_angle(600, -1000, then=Stop.HOLD, wait=False)
robot.turn(angle=75, wait=True)
robot.straight(distance=-215, wait=True)
main_motor.run_angle(600, 300, then=Stop.HOLD)
robot.turn(angle=-25, wait=True)
robot.straight(distance=100, wait=True)
robot.turn(angle=-45, wait=True)
robot.straight(distance=-600, wait=True)
robot.arc(radius=-400, angle=-80, wait=True)
robot.straight(distance=-450, wait=True)








