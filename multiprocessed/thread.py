﻿__author__ = 'Administrator'
'''
Python主要通过标准库中的threading包来实现多线程

 '''
# A program to simulate selling tickets in multi-thread way
# Written by Vamei

import threading
import time
import os

# This function could be any function to do other chores.
def doChore():
    time.sleep(0.5)

# Function for each thread
def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()                # Lock; or wait if other thread is holding the lock
        if i != 0:
            i = i - 1                 # Sell tickets
            print(tid,':now left:',i) # Tickets left
            doChore()                 # Other critical operations
        else:
            print("Thread_id",tid," No more tickets")
            os._exit(0)              # Exit the whole process immediately
        lock.release()               # Unblock
        doChore()                    # Non-critical operations

# Start of the main function
i    = 100                           # Available ticket number
lock = threading.Lock()              # Lock (i.e., mutex)

# Start 10 threads
for k in range(10):
    new_thread = threading.Thread(target=booth,args=(k,))   # Set up thread; target: the callable (function) to be run, args: the argument for the callable
    new_thread.start()   
	# run the thread
	
	
"""
我们在函数中使用global来声明变量为全局变量，
从而让多线程共享i和lock (在C语言中，我们通过将变量放在所有函数外面来让它成为全局变量)。
如果不这么声明，由于i和lock是不可变数据对象，它们将被当作一个局部变量(参看Python动态类型)。
如果是可变数据对象的话，则不需要global声明。我们甚至可以将可变数据对象作为参数来传递给线程函数。
这些线程将共享这些可变数据对象。
我们在booth中使用了两个doChore()函数。可以在未来改进程序，
以便让线程除了进行i=i-1之外，做更多的操作，比如打印剩余票数，找钱，或者喝口水之类的。
第一个doChore()依然在Lock内部，所以可以安全地使用共享资源 (critical operations, 
比如打印剩余票数)。第二个doChore()时，Lock已经被释放，所以不能再去使用共享资源。
这时候可以做一些不使用共享资源的操作 (non-critical operation, 比如找钱、喝水)。
我故意让doChore()等待了0.5秒，以代表这些额外的操作可能花费的时间。
你可以定义的函数来代替doChore()。


"""	
	