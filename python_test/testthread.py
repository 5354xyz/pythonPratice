# -*- coding: utf8 -*- 
import time
import sys
import datetime

#在同一个目录下面可以直接引用
import MyThread
def fib(x):
    time.sleep(0.05)
    if x<2:return 1
    return (fib(x-2) +fib(x-1))
def fac(x):
    time.sleep(0.1)
    if x<2:return 1
    return (x*fac(x-1))
def sum_(x):
    time.sleep(0.1)
    if x<2:return 1
    return x+sum_(x-1)
funcs = [fib,fac,sum_]
n=12

def main():
    nfuncs = range(len(funcs))
    print '******SINGLE THREAD START******'
    Tstarttime = datetime.datetime.now()
    Sstarttime = datetime.datetime.now()
    for i in nfuncs:
        print 'start ',funcs[i].__name__,'at : ',\
              time.ctime()
        starttime = datetime.datetime.now()
        print funcs[i](n)
        endtime = datetime.datetime.now()
        print funcs[i].__name__,(endtime - starttime).seconds,'s'
        print funcs[i].__name__,'finnished ','at : ',\
              time.ctime()

    Sendtime = datetime.datetime.now()
    print 'SINGLE THREAD TIME ',(Sendtime - Sstarttime).seconds,'s'
    Mstarttime = datetime.datetime.now()
    print '******MULTIPLE THREAD START*****'
    threads = []#用来存放线程
    for i in nfuncs:
        #MyThread.MyThread,要注意，不要直接MyThread只是模块，要引用到里面的类才行，否则
        #报TypeError: 'module' object is not callable 错误
        t = MyThread.MyThread(funcs[i],(n,),funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        #当前进程的其他线程调用了join方法之后，会阻塞当前进程等待其他线程执行完在往下执行，可以给join设置超时参数
        threads[i].join()
        print i
        print threads[i].getResult()
    Mendtime = datetime.datetime.now()
    
    print 'MULTIPLE THREAD TIME ',(Mendtime - Mstarttime).seconds,'s'
    Tendtime = datetime.datetime.now()
    print 'TOTAL TIME ',(Tendtime - Tstarttime).seconds,'s'
    print 'ALL DONE'

if __name__ == '__main__':
    main()
