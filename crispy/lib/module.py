import logging

logger = logging.getLogger(__name__)

class CrispyModule(object):
    """ Module object that all other modules will inherit from. """
    
    def __init__(self, client):
	self.client = client

    def check_args(self, args):
	""" Override this method to define your own arguments. """
	return True

    def is_compatible(self):
	""" Override this method to define if module is compatible with the given client. """
	if "all" in self.compatible_systems:
	    return (True, "")
	elif "windows" in self.compatible_systems and self.client.is_windows():
	    return (True, "")
	elif "linux" in self.compatible_systems and self.client.is_linux():
	    return (True, "")
	elif "darwin" in self.compatible_systems and self.client.is_darwin():
	    return (True, "")
	elif "unix" in self.compatible_systems and self.client.is_unix():
	    return (True, "")
	else:
	    return (False, "This module currently only supports the following systems: %s" (','.join(self.compatible_systems)))
