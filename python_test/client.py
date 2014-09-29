import socket
HOST ='localhost'#www.baidu.com
PORT = 13651
BUFSIZE = 1024
ADDR =(HOST,PORT)
try:
    tcpClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpClientSock.connect(ADDR)
except Exception as e:
    print e


while True:
    data = raw_input('please input the meassage send to server:')
    if not data:
        break
    print data
    try:
        tcpClientSock.send(data)
        data = tcpClientSock.recv(BUFSIZE)
    except Exception as e:
        print e
    if not data:
        break
    print data
tcpClientSock.close()
