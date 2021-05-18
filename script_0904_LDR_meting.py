from gpiozero import LightSensor

varSensor = LightSensor(18)
print(varSensor.value)