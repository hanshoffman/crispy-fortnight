import platform
import socket
import sys

from os_types import macintosh
from os_types import windows

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
    
    if not data: 
        break
    elif data == "enum_os":
        if platform.system() == 'Darwin':
            conn.send(macintosh.enum_os())
        elif platform.system() == 'nt':
            print "needs to be implemented"
            #conn.send(windows.enum_os())
        else:
            break
    elif data == "enum_printers":
        if platform.system() == 'Darwin':
            conn.send(macintosh.enum_printers())
    elif data == "enum_applications":
        if platform.system() == 'Darwin':
            conn.send(macintosh.enum_applications())
    else:
        print "unknown command"
         
conn.close()