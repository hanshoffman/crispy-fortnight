import platform
import socket
import sys

from os_types.macintosh import *

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
MAX_CONN = 1
BUFFER_SIZE = 1024

#re-write to include try except
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(MAX_CONN)
except socket.error, (value,message):
    if s: 
        s.close() 
    print "Could not open socket: " + message 
    sys.exit(1)

while True:
    conn, addr = s.accept()
    data = conn.recv(BUFFER_SIZE)
    
    if not data: 
        break
    elif data == "enum_os":
        if platform.system() == 'Darwin':
            conn.send(enum_os())
    elif data == "enum_printers":
        if platform.system() == 'Darwin':
            conn.send(enum_printers())
    elif data == "enum_applications":
        if platform.system() == 'Darwin':
            conn.send(enum_applications())
    else:
        print "another os needs to be implemented"
    
        
conn.close()