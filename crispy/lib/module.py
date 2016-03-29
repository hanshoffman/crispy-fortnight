import StringIO

class CrispyModule(object):
    compatible_systems = []
    category = "general"

    def __init__(self, client, job):
	self.client = client
	self.job = job
	self.stdout = StringIO.StringIO()

    def init_argparse(self):
	"""Override this method to define your own arguments."""
	pass

    def is_compatible(self):
	"""Override this method to define if module is compatible with the given client."""
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

    def log(self, msg):
	self.stdout.write(msg)

    def error(self, msg)
	self.stdout.write(msg)

    def warning(self, msg)
	self.stdout.write(msg)

    def success(self, msg)
	self.stdout.write(msg)

    def info(self, msg)
	self.stdout.write(msg) 
