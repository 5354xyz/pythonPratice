# -*- coding: cp936 -*-
class BeingTest (object):
    def __init__(self):
        pass
    def fib(self,x):
        if x<2:return 1
        #python ���治��ֱ�ӵ��ñ���ĺ���
        return (self.fib(x-2) +self.fib(x-1))
    def fac(self,x):
        print 'i am from beTest',x
        if x<2:return 1
        return (x*self.fac(x-1))
    def sum_(self,x):
        if x<2:return 1
        return x+self.sum_(x-1)
    
