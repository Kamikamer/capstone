import time

from eel import sleep

class Stopwatch:
    _instance = None

    def __new__(cls):
      if not hasattr(cls, 'instance'):
        cls.instance = super(Stopwatch, cls).__new__(cls)
      return cls.instance
    
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def stop(self):
        if self.running:
            self.end_time = time.time()
            self.elapsed_time = self.end_time - self.start_time
            self.running = False

    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0
        self.running = False

    def get_elapsed_time(self):
        if self.running:
            self.end_time = time.time()
            self.elapsed_time = self.end_time - self.start_time
        return round(self.elapsed_time, 2)

    def is_running(self):
        return self.running
    

if __name__ == "__main__":
    Stopwatch = Stopwatch()
    Stopwatch.start()
    sleep(4)
    print(Stopwatch.get_elapsed_time())
    sleep(3)
    print(Stopwatch.get_elapsed_time())
