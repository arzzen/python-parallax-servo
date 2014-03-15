#!/usr/bin/env python
import time
import sys
sys.path.append('modules')
import ParallaxServoController as PSC
import ParallaxServoHandler as PSH

rate = 3
servo = PSC.ParallaxServoController('COM7', baudrate=2400)
handler = PSH.ParallaxServoHandler(servo)

servo.setHomePosition(rate)
time.sleep(7)

handler.setX(1)
handler.setY(1)
handler.setZ(1)

handler.setLengthA(15)
handler.setLengthB(20)
handler.setLengthC(10)

handler.findPosition()




