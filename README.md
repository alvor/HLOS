# HydroLED Operation System 

## ESP32 based micro system, for remote control this device
```
This code must be upload to ESP32 chip microPython based 
```



## Structure code
```

main.py - файл конфигурации этого устройства


modules - папка для модулей расширения, каждый модуль это файл или папка принадлежащий(я)
 каждой отдельной единицы внутреннего модуля устройства.
 Каждый модуль работает в постоянном асинхронном цикле 
 Свойство "state"
 {uid:'sensor_dev_15559', name: 'name_of_unit', time:0, data:"any data"}
 time - последнее измененное состояние, если изменений небыло время не меняется 
 data - блок инфыормации содержащий произвольные данные

```

/libs - папка с библиотеками расширяющих возможности устройства
/modules - модули расширения устройства, 

/web/ui - папка с вашим интерфейсом для этого проекта,


### Customize configuration

