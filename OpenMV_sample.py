# Untitled - By: aoiyamanaka - 月 6月 12 2023

import time
from pyb import UART,LED

led=pyb.LED(3)
uart=UART(3,115200,timeout_char=1000)

while True :
    uart.writechar(100)
    led.toggle()
    time.sleep_ms(1000)
