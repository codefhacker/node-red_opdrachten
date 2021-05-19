from gpiozero import LightSensor

varSensor = LightSensor(18)


if varSensor.value <= 0.5:
    print(int(1))
    
    
