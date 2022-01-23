#purpose: to go different directions and take pictures, with a press of a key
#CREATED BY: RIA RAO for CRTC 2022
from djitellopy import tello
import keypressModule as kp
import time
import cv2
global img

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 30

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("u"): ud = speed
    elif kp.getKey("d"): ud = -speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("c"): yv = speed

    if kp.getKey("v"): me.land(); time.sleep(3)
    elif kp.getKey("t"): me.takeoff()

    if kp.getKey('s'):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(1)

    return [lr, fb, ud, yv]


me.takeoff()

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    # img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)

