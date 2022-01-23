# purpose: for the drone to fly different directions with presses of keys
#CREATED BY: RIA RAO for CRTC 2022
from djitellopy import tello
import keypressModule as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 30

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("u"): ud = speed
    elif kp.getKey("d"): ud = -speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("c"): yv = speed

    if kp.getKey("v"): me.land()
    elif kp.getKey("t"): me.takeoff()

    return [lr, fb, ud, yv]


me.takeoff()

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep (1)



