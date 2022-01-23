#purpose: to autonomously follow a set perimeter
#CREATED BY: RIA RAO for CRTC 2022

from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()
me.send_rc_control(0,23,0,0) #forward (w)
sleep(4)
me.send_rc_control(0,0,0,37) #rotate
sleep(4)
me.send_rc_control(0,28,0,0) ##forward (l)
sleep(4)
me.send_rc_control(0,0,0,33) #rotate
sleep(4)
me.send_rc_control(0,25,0,0) #forward (w)
sleep(4)
me.send_rc_control(0,0,0,39) #rotate
sleep(4)
me.send_rc_control(0,39,0,0) #forward (l)
sleep(3)
me.send_rc_control(0,0,0,40) #rotate
sleep(4)
me.land()