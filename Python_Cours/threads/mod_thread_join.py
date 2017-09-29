import threading as th
import time
import logging

def fct_daemon(*t):
    print("execution:", t[0])
    time.sleep(20)
    print("finish:", t[0])


def fct_nondaemon(*t):
    print("execution:", t[0])
    print("finish:", t[0])

def main():
    ##thread creation
    thread_deamon = th.Thread(name='first_d',target=fct_daemon,args=("daemon",))
    thread_ndeamon = th.Thread(name='first', target=fct_nondaemon, args=("non daemon",))

    thread_deamon.setDaemon(True)
    thread_deamon.start()
    thread_ndeamon.start()

    thread_deamon.join()



if __name__ == '__main__':
    main()

