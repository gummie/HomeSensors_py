from modules.sensorcontrol import SensorControl
from modules.arduinocontrol import ArduinoControl
from queue import Queue
import  threading
import time

# sens = SensorControl
# ardc = ArduinoControl
#
# sens.run_sensors()
# ardc.arduino_comm()
#
# print("Hallo")

def process_data(threadName, q):
    while not exitFlag:
        Queue.queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            Queue.queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            Queue.queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
#threadList = [SensorControl]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
    thread = SensorControl(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")