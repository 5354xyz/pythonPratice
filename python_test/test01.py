# -*- coding: utf8 -*-
d1={'tudou':3,'yangcong':1,'mitao':8}
d2={'mitao':3,'pantao':5,'wutongshu':2,'bailian':1}
d1.update(d2)
print d1
sample_list = ['a',1,('a','b')]
for element in sample_list:
    print(element)
l1=(1,2,3,4)
print zip(l1,sample_list)
print type(zip(l1,sample_list))
dict2=dict(zip(l1,sample_list))
print dict2
b=[ '1:0.1', '2:0.0', '3:0.7', '4:0.2', '5:0.0', '6:0.4']
c = dict(eval(i.replace(":",",")) for i in b)
print c
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 3
high = 7
alistback = filter(lambda x, l=low, h=high: h>x>l, aList) # returns: [4, 5, 6]
print alistback
print type(alistback)
f = (lambda x: x + 2)
print f(0)
print type(alistback)
dict01={'host':'baidu.com','port':100}
dict02={'host':'baidu.com','port':90,'xyz':'xiaoyizong'}
#比较字典，(优先级为元素个数、键大小、键值大小)
print cmp(dict01,dict02)
print str(dict01)
sum=reduce(lambda x,y:x+y,(1,2,3,4,5,6,7))
print sum
def myadd(x,y):   
    return x + y  
sum=reduce(myadd,(1,2,3,4,5,6,7,8))   
print sum
L = [(lambda x: x**2),
	(lambda x: x**3),
	(lambda x: x**4)]
print L[0](2),L[1](2),L[2](2)

D = {'f1':(lambda: 2+3),
	'f2':(lambda: 2*3),
	'f3':(lambda: 2**3)}
print D['f1'](),D['f2'](),D['f3']()
print [x**2 for x in range(10)]
print map((lambda x: x**2), range(10))
def addlist(alist):
    for i in alist:
        yield i + 1
alist = [1, 2, 3, 4]
for x in addlist(alist):
    print x,
integer =[1,6,3,8,5,3,11]
for v in range(7):
#for i,v in enumerate(integer):       
	if v == 3:
	    print (' v 是\
	   3.')
	    print ('''我也是在if之后执行的。''')
	elif v < 3:
	    print ('v < 3')
	elif v>=3 and v<10:
	    print ('大于等于3，小于10。')
	else:
		print("其他情况")
	print(v)

print ('打印结束。')
