import uasyncio as asyncio
from libs.kernel import Service
from machine import Pin

class PumpOnGPIO(Service):
    def __init__(self):
        super().__init__(**kwargs)


    async def start(self, pin, duration):
        _p = Pin(pin, Pin.OUT)

        # Включаем насос
        _p.value(1)

        # Обновляем состояние, аналогично как в GPIO_board
        for i in self.state['data']:
            if i['id'] == pin and i.get("control"):
                i['value'] = _p.value()  # Обновляем значение состояния
                self.state['time'] = time.time()
                asyncio.create_task(self.subscribe_handler())  # Обработчик событий (по аналогии с GPIO_board)

        # Ожидаем заданную продолжительность
        await asyncio.sleep(duration)

        # Выключаем насос
        _p.value(0)

        # Снова обновляем состояние
        for i in self.state['data']:
            if i['id'] == pin and i.get("control"):
                i['value'] = _p.value()  # Обновляем значение состояния
                self.state['time'] = time.time()
                asyncio.create_task(self.subscribe_handler())  # Обработчик событий
