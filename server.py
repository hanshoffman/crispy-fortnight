from crispy.implantHandler import ImplantHandler
from crispy.implantServer import ImplantServer

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080  

    try:
        server = ImplantServer((HOST, PORT), ImplantHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print ""
        server.shutdown()
        server.socket.close()
        