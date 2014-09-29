# clientsocket.py

import socket

def Main():
    try:
        # Address Family : AF_INET (this is IP version 4 or IPv4)
        # Type :  SOCK_STREAM (this means connection oriented TCP protocol)
        #         SOCK_DGRAM indicates the UDP protocol. 
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to creat socket. Error code:', str(msg[0]), 
        print 'Error message:', msg[1]
        return
    print 'Socket Created'
    
    host = 'www.baidu.com'
    port = 80
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting.'
        return 
    print 'Ip address of', host, 'is', remote_ip
    
    # Connect to remote server
    new_socket.connect((host, port))
    print 'Socket Connected to', host, 'on ip', remote_ip
    
    # Send some data to remote server | socket.sendall(string[, flags]) 
    message = 'GET / HTTP/1.1\r\n\r\n'
    try:
        new_socket.sendall(message)
    except socket.error:
        print 'Send fail.'
        return 
    print 'Message send successfully.'

    # Receive data | socket.recv(bufsize[, flags]) 
    reply = new_socket.recv(4096)
    print reply
    
    # Close the socket
    new_socket.close()
    
    
if __name__ == '__main__':
    Main()
