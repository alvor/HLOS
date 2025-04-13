import uasyncio as asyncio
from libs.kernel import Service
from machine import Pin

class PumpOnGPIO(Service):
    def __init__(self):
        pass

    def start(self, pin, duration):
        _p=Pin(pin,Pin.OUT)
        _p.value(1)


