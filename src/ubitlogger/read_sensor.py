# type: ignore

"""MicroPython script template used by ubitlogger

Script starts reading a sensor (temperature, light, accelerometer) when
you hold down the left button until a check mark is displayed on the micro:bit.
If the right button is pushed and held down until a cross mark displays, the
micro:bit stops reading the sensor. Readings are send to ubitlogger over the
serial link.
"""

from microbit import *

print('start')
reading = False
while True:
    if button_a.is_pressed():
        reading = True
        display.show(Image.YES)
        sleep(3000)
        display.clear()
    if button_b.is_pressed():
        reading = False
        display.show(Image.NO)
        sleep(3000)
        display.clear()
        print('Stopped')
    if reading:
        print({% function %}())
    sleep(2000)