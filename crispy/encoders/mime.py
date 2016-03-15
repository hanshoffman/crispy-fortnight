import base64

class Mime:
    def encode(self, data):
        return base64.b64encode(data)
    
    def decode(self, data):
        return base64.b64decode(data)