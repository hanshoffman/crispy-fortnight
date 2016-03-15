import socket
import sys

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
    info = "\nRemote commands:\n"
    info += "\tenum_os            - get operating system info\n"
    info += "\tenum_interfaces    - get a list of interfaces\n"
    info += "\tenum_applications  - get a list of installed applications\n"
    info += "\tenum_drives        - get a list of drives\n"
    info += "\tenum_printers      - get a list of printers\n"
    info += "\tenum_usb           - get a list of USBs\n"
    info += "\tget_reboot_history - get the system reboot history\n"
    info += "\tget_process_list   - get the system process list\n"
    info += "\tget_ssh_keys       - get any ssh keys\n"
    info += "Local commands:\n"
    info += "\tsession            - show current session\n"
    info += "\texit               - close down connection to remote host\n"
     
    return info
 
def get_session_info():
    # show length of connection
    # show remote ip and port connected to
    return "need to implement once bind/reverse conn is figured out"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
            sock.sendall(commandToExecute + "\n")
            data = sock.recv(BUFFER_SIZE)
            print data
except:
    print "Couldn't connect to " + TCP_IP
finally:
    sys.exit(0)