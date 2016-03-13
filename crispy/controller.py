import socket
import subprocess

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
MAX_CONN = 1
BUFFER_SIZE = 1024
PROMPT = "%s:%i>> " %(TCP_IP, TCP_PORT)
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
    info += "\tenum_users         - get a list of users\n"
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
    #show length of connection
    #show remote ip and port connected to
    return "need to implement once bind/reverse conn is figured out"
    
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    print(BANNER)
except socket.error, (value, message): 
    if s: 
        s.close() 
    print "Could not connect to server: " + message 
    sys.exit(1) 

while True:
    commandToExecute = raw_input(PROMPT).strip().lower()
    
    if commandToExecute == '-h' or commandToExecute == 'help':
        print help_menu()
    elif commandToExecute == 'session':
        print get_session_info()
    elif commandToExecute == 'exit' or commandToExecute == 'quit':
        break
    else:
        s.send(commandToExecute)
        data = s.recv(BUFFER_SIZE)
        print data
        
s.close()

#write method to pass connection off to someone else??