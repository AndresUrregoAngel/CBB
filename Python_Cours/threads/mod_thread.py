# __*__UTF-8 __*__
import threading as th
import time

def funtion (a,b):
    z= a+b
    time.sleep(2)
    print('testing function in a thread:', z)

#is capable to execute the same process twice
thread_base = th.Thread(None,target=funtion,name='t1',args=(2,3))
thread_base.run()
thread_base = th.Thread(None,target=funtion,name='t2',args=(5,5))
thread_base.run()


#this will run in one shoot without share the same execution with the tread
funtion(3,3)

