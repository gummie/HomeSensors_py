from modules.sensorcontrol import SensorControl
from modules.arduinocontrol import ArduinoControl

sens = SensorControl
ardc = ArduinoControl

sens.run_sensors()
ardc.arduino_comm()

print("Hallo")