from threading import Thread

class MyThread(Thread):
    def __init__(self, event, payloadFunc = None, interval = 10.0):
        Thread.__init__(self)
        self.stopped = event
        self.payloadFunc = payloadFunc
        self.interval = interval

    def run(self):
        while not self.stopped.wait(self.interval):
            self.payloadFunc()
