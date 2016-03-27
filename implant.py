# from crispy.controller import CrispyController
# from crispy.crypto.mime import Mime
# 
# if __name__ == "__main__":
#     cc = CrispyController("localhost", 8080, Mime())
#     cc.run()

from crispy.network.client_types import CrispyTCPClient

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    
    sock = CrispyTCPClient().connect(HOST, PORT)
    print sock.recv(1024)