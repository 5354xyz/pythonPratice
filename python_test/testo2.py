# -*- coding: utf8 -*-
integer =[1,6,3,8,5,3,11]
for v in range(len(integer)):
#for i,v in enumerate(integer):       
	if integer[v] == 3:
	    print (' v 是\
	   3.')
	    print ('''我也是在if之后执行的。''')
	elif integer[v] < 3:
	    print ('v < 3')
	elif integer[v]>=3 and integer[v]<10:
                print ('大于等于3，小于10。')
        else:
                print('其他情况')
	print(integer[v])

print ('打印结束。')

import sys
print 'you enterd' , len(sys.argv),'arguments...'
print 'they were ', str(sys.argv)
class Sample:
    def __enter__(self):
        return self
 
    def __exit__(self, type, value, trace):
        print "type:", type
        print "value:", value
        print "trace:", trace
 
    def do_something(self):
        bar = 1/0
        return bar + 10
 
with Sample() as sample:
    sample.do_something()
