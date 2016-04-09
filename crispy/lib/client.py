import logging

logger = logging.getLogger(__name__)

class CrispyClient(object):
    def __init__(self, desc):
        self.desc = desc
        self.conn = self.desc["conn"]
    
    def __str__(self):
        """ Return string representing a CrispyConnection object (full). """
        logger.debug("__str__() was called")
	return "CrispyClient(id=%d, ip=%s, macaddr=%s, hostname=%s, platform=%s, proc_type=%s, proc_arch=%s, uptime=%s, date=%s, user=%s, home=%s, shell=%s)" %(
		self.desc["id"], self.desc["ip"], self.desc["macaddr"], self.desc["hostname"], self.desc["plat"], self.desc["proc_type"], 
		self.desc["proc_arch"], self.desc["uptime"], self.desc["date"], self.desc["user"], self.desc["home"], self.desc["shell"])

    def get_session(self):
	"""" Return socket for this CirspyClient object. """
	return self.desc["conn"]

    def get_id(self):
	""" Return id for this CirspyClient object. """
	return self.desc["id"]

    def short_name(self):
	""" Return string representing a CrispyConnection object (short). """
	logger.debug("short_name() was called")
	return "CrispyClient(id=%d, user=%s, platform=%s, hostname=%s, macaddr=%s)" %(self.desc["id"], self.desc["user"], self.desc["plat"], self.desc["hostname"], self.desc["macaddr"]) 

    def is_android(self):
        """ Determine if platform connected is an Android device. """
	logger.debug("is_android() was called")
        if "Android" in self.desc["plat"]:
            return True
        else:
            return False
    
    def is_darwin(self):
        """ Determine if platform connected is a Macintosh system. """
        logger.debug("is_darwin() was called")
	if "Darwin" in self.desc["plat"]:
            return True
        else:
            return False
    
    def is_linux(self):
        """ Determine if platform connected is an Linux system. """
        logger.debug("is_linux() was called")
	if "Linux" in self.desc["plat"]:
            return True
        else:
            return False
    
    def is_windows(self):
        """ Determine if platform connected is a Windows system. """
        logger.debug("is_windows() was called")
	if "Windows" in self.desc["plat"]:
            return True
        else:
            return False

    def is_unix(self):
	""" Determine if platform connected is a *nix system. """
	logger.debug("is_unix() was called")
	return not self.is_windows()
    
    def is_proc_arch_64_bits(self):
        """ Determine if platform connected is a 64-bit architecture. """
        logger.debug("is_proc_arch_64_bits() was called")
	if "64" in self.desc["proc_arch"]:
            return True
        else:
            return False

    def run_module(self, module, args):
	""" Start a module on client. """
	logger.debug("run_module() was called")
	#get module name
	#try catch module.run(args)
	pass
