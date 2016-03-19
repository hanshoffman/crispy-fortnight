from crispy.implant import ImplantHandler
from crispy.encoders.mime import Mime

if __name__ == "__main__":
    implant = ImplantHandler("localhost", 8080, Mime())
    implant.run()