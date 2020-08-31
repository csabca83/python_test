import time

class Functions:
    def function1(self):
        t = time.localtime()
        self.value = time.strftime("%H:%M:%S", t)