import socket
import time
HOST = ''
PORT = 13651
BUFSIZE = 1024
ADDR =(HOST,PORT)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(10)#��ʾ��� �����Ӷ��ٸ�

while True:
    print 'wating for connection ...'
    tcpCliSock , addr = tcpSerSock.accept()
    print 'connecting from : %s' % str(addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (time.ctime(),data))
        
    tcpCliSock.close()#����ط�ע��һ�£���ѭ���������ٹص�
    print 'tcpCliSock.close()'
tcpSerSock.close()                  
    
