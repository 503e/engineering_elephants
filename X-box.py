from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color, Button
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.iodevices import XboxController

hub = PrimeHub()
controller = XboxController()

main_motor = Motor(Port.F, Direction.CLOCKWISE)
left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)


    

while True:
    # Get the joystick values from the Xbox controller
    steering_input = controller.joystick_left()[0]  # Left joystick X-axis
    throttle_input = controller.joystick_left()[1]  # Left joystick Y-axis
    motor_input = controller.joystick_right()[1]  # Right joystick Y-axis
    #print("steering:", steering_input, "throttle:", throttle_input, "motor:", motor_input)
    throttle = throttle_input*5
    buttonvolose = controller.buttons.pressed()
    if Button.B in buttonvolose:
        print("B pressed")
        hub.speaker.beep(frequency=100, duration=500)


    robot.drive(throttle, steering_input)
    motor_input = motor_input*3
    main_motor.run(motor_input)


    wait(10)  # Small delay to prevent overwhelming the CPU