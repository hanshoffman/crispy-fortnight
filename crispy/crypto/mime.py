import base64
import logging

logger = logging.getLogger(__name__)

class Mime:
    """ Simple mime base64 encoding/decoding. """
    
    def encode(self, data):
	logger.debug("b64 encode() called")
        return base64.b64encode(data)
    
    def decode(self, data):
	logger.debug("b64 decode() called")
        return base64.b64decode(data)
