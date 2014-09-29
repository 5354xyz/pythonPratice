import socket
import time
HOST = ''
PORT = 13651
BUFSIZE = 1024
ADDR =(HOST,PORT)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(10)#表示最多 能连接多少个

while True:
    print 'wating for connection ...'
    tcpCliSock , addr = tcpSerSock.accept()
    print 'connecting from : %s' % str(addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (time.ctime(),data))
        
    tcpCliSock.close()#这个地方注意一下，是循环结束后再关掉
    print 'tcpCliSock.close()'
tcpSerSock.close()                  
    
