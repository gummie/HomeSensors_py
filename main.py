from modules.sensorcontrol import SensorControl
from modules.arduinocontrol import ArduinoControl
from queue import Queue
import threading
import time
import sqlite3

threadPool = Queue()

threadList = [SensorControl, ArduinoControl]
threads = []

sensorThread = SensorControl('sensorThread', threadPool)
threads.append(sensorThread)
arduinoThread = ArduinoControl('AdrduinoThread', threadPool)
threads.append(arduinoThread)

print("Number of active threads:", threading.active_count())

for t in threads:
    t.start()

# sensorThread.start()
# arduinoThread.start()

print("Number of active threads:", threading.active_count())

for t in threadList:
    threadPool.put(t)

print("Number of active threads:", threading.active_count())

# threadPool.join()

print("Queue size:", threadPool.qsize())

for t in threads:
    t.join()

# sensorThread.join()
# arduinoThread.join()

for t in threads:
    print("Thread is alive:", t.is_alive())

print("Exiting Main Thread")

print("Number of active threads:", threading.active_count())