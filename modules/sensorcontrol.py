from queue import Queue
import threading
import time

class SensorControl(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        print("Starting " + self.name)
        while True:
            i = self.queue.get()
            print(i)
            self.queue.task_done()
        #run_sensors(self.name, self.q)
        print("Exiting " + self.name)

    # def run_sensors(threadname, queue):
    #     print("Run sensors")
    #     while not exitFlag:
    #         if not queue.WokQueue.empty():
    #             data = queue.get()
    #             queue.queueLock.release()
    #             print("%s processing %s" % (threadName, data))
    #         else:
    #             q.queueLock.release()
    #         time.sleep(1)

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