from queue import Queue
import threading
import time

exitFlag = 0

class SensorControl(threading.Thread):

    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Starting " + self.name)
        #run_sensors(self.name, self.q)
        print("Exiting " + self.name)

    def run_sensors(threadname, q):
        print("Run sensors")
        while not exitFlag:
            if not q.WokQueue.empty():
                data = q.get()
                q.queueLock.release()
                print("%s processing %s" % (threadName, data))
            else:
                q.queueLock.release()
            time.sleep(1)

# def process_data(threadName, q, workQueue):
#     while not exitFlag:
#         Queue.queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             Queue.queueLock.release()
#             print("%s processing %s" % (threadName, data))
#         else:
#             Queue.queueLock.release()
#         time.sleep(1)