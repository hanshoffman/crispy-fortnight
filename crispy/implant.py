import platform
import socket
import sys

from os_types import macintosh
#from crispy.os_types.debian import Debian

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
MAX_QUEUE_SIZE = 1
BUFFER_SIZE = 1024

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(MAX_QUEUE_SIZE)
except socket.error, (value, message):
    if s: 
        s.close()
    sys.exit(1)

while True:
    conn, addr = s.accept()
    data = conn.recv(BUFFER_SIZE)
    #https://docs.python.org/3.4/howto/sockets.html
    #https://docs.python.org/3/library/socketserver.html
    
    #use polymorphism to remove lengthy if/else?
    #https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
    #deb = Debian()
    #deb.lp()
            
    if data == "enum_os":
        if platform.system() == 'Darwin':
            conn.send(macintosh.enum_os())
            #use encoder first, then send request
    elif data == "enum_printers":
        if platform.system() == 'Darwin':
            conn.send(macintosh.enum_printers())
    elif data == "enum_applications":
        if platform.system() == 'Darwin':
            conn.send(macintosh.enum_applications())
    elif data == "enum_users":
        if platform.system() == 'Darwin':
            conn.send(macintosh.enum_users())
    elif data == 'upload':
        conn.send("still working on")
    else:
        conn.send("unknown command")
         
conn.close()