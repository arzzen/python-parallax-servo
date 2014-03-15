
python-parallax-servo
=====================

Parallax Serial Servo Handler.

Simple usage
=====================
```
servo = PSC.ParallaxServoController('COM7', baudrate=2400)
handler = PSH.ParallaxServoHandler(servo)

handler.setX(1)
handler.setY(1)
handler.setZ(1)

handler.setLengthA(15)
handler.setLengthB(20)
handler.setLengthC(10)

handler.findPosition()
```


