from modules.sensorcontrol import SensorControl
from modules.arduinocontrol import ArduinoControl
from queue import Queue
import threading
import time

exitFlag = 0

# sens = SensorControl
# ardc = ArduinoControl
#
# sens.run_sensors()
# ardc.arduino_comm()

threadPool = Queue()

# for i in range(5):
#     t = SensorControl(threadPool)

sensorThread = SensorControl(threadPool)

sensorThread.start()

threadPool.put(SensorControl)

print('Thread is alive:', sensorThread.is_alive())
print("Number of active threads:", threading.active_count())

# Fill the queue
# for i in range(5):
#     threadPool.put(i)

#queueLock.release()

# Wait for queue to empty
# while not threadPool.empty():
#     pass

# Notify threads it's time to exit
# exitFlag = 1

# Wait for all threads to complete
# for t in threads:
#     t.join()
threadPool.join()
print("Exiting Main Thread")