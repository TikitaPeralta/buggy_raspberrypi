from bluedot import BlueDot
from gpiozero import Robot
from signal import pause

bd = BlueDot()
bd.color = "red"

robot = Robot(left=(27, 22), right=(25, 4))

def move(pos):
    if pos.top:
        robot.forward()
    elif pos.bottom:
        robot.backward()
    elif pos.left:
        robot.left()
    elif pos.right:
        robot.right()

def stop():
    robot.stop()

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

pause()