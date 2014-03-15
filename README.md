
python-parallax-servo
=====================

Parallax Serial Servo Handler.

Servo motor controller. Simple interface for Parallax microcontroller.

Tested with "Parallax Continuous Rotation Servo"

![parallax servo](http://www.parallax.com/sites/default/files/styles/mid-sized-product/public/900-00008.png?itok=ivl060qw "Parallax Continuous Rotation Servo")



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


