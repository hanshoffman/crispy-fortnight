from crispy.controller import CrispyController
from crispy.encoders.mime import Mime

if __name__ == "__main__":
    cc = CrispyController()
    cc.run("localhost", 8080, Mime())
