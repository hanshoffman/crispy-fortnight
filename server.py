import SocketServer

from crispy.implantHandler import ImplantHandler

if __name__ == "__main__":
    #implant = Implant("localhost", 8080, Mime())
    #implant.run()
    
    HOST, PORT = "localhost", 8080

    try:
        SocketServer.TCPServer.allow_reuse_address = True
        server = SocketServer.TCPServer((HOST, PORT), ImplantHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.socket.close()