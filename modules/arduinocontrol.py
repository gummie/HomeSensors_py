import threading

class ArduinoControl(threading.Thread):

    def __init__(self, threadname, queue):
        threading.Thread.__init__(self)
        self.name = threadname
        self.queue = queue

    def run(self):
        print("=========== Starting " + self.name + " ===========")
        self.arduino_comm()
        # while True:
        # i = self.queue.get()
        # print(i)
        # self.queue.task_done()
        #run_sensors(self.name, self.q)
        print("=========== Exiting " + self.name + " ===========")

    def arduino_comm(self):
        print("Run Arduino...")