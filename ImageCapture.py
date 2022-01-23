#purpose: for drone to take pictures w/ a press of a key
#CREATED BY: RIA RAO for CRTC 2022

from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
