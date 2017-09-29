import threading as th
import time

class MaThreadh(th.Thread):

    def run(self):
        time.sleep(5)
        return

for i in range(3):
    t=MaThreadh()
    t.start()
    print("T is alive", t.is_alive())