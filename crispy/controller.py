import socket
import subprocess

PORT = 443
MAX_CONN = 5
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
    \__\/         \__\/                     \__\/         \__\/                "
     
def clear():
    subprocess.call(["clear"])
    
def connect():
    print "Connect"
    
def myreceive(self):
    chunks = []
    bytes_recd = 0
    while bytes_recd < MSGLEN:
        chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
        if chunk == '':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    return ''.join(chunks)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((socket.gethostname(), PORT))
serverSocket.listen(MAX_CONN)

#clear()
print(BANNER)
while true:
    (clientsocket, address) = serverSocket.accept()
    print("Connection from: " + str(address))
    commandToExecute = input(">> ")
    
    if commandToExecute == "help":
        print "commands..."
