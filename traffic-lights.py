from ev3dev2.led import Leds
import time
Dmitry=Leds()
while True:
  Dmitry.set_color("LEFT", "RED")
  Dmitry.set_color("RIGHT", "RED")
  time.sleep(1)
  Dmitry.set_color("LEFT", "AMBER")
  Dmitry.set_color("RIGHT", "AMBER")
  time.sleep(1)
  Dmitry.set_color("LEFT", "GREEN")
  Dmitry.set_color("RIGHT", "GREEN")
  time.sleep(1)
