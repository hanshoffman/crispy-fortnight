class CrispyConnection(object):
    def __init__(self, desc):
        self.desc = desc
        self.conn = self.desc["conn"]
    
    def __str__(self):
        """Return string representing a CrispyConnection object (full)."""
        return "Connection(id=%d, user=%s, platform=%s, hostname=%s, macaddr=%s)" %(self.desc["id"], self.desc["user"], self.desc["platform"], self.desc["hostname"], self.desc["macaddr"])
    
    def short_name(self):
	"""Return string representing a CrispyConnection object (short)."""
	return self.desc["platform"][:3].lower() + "_" + self.desc["hostname"] + "_" + self.desc["macaddr"] 

    def is_android(self):
        """Determine if platform connected is an Android device."""
        if "Android" in self.desc["platform"]:
            return True
        else:
            return False
    
    def is_darwin(self):
        """Determine if platform connected is a Macintosh system."""
        if "Darwin" in self.desc["platform"]:
            return True
        else:
            return False
    
    def is_linux(self):
        """Determine if platform connected is an Linux system."""
        if "Linux" in self.desc["platform"]:
            return True
        else:
            return False
    
    def is_windows(self):
        """Determine if platform connected is a Windows system."""
        if "Windows" in self.desc["platform"]:
            return True
        else:
            return False

    def is_unix(self):
	"""Determine if platform connected is a *nix system."""
	return not self.is_windows()
    
    def is_proc_arch_64_bits(self):
        """Determine if platform connected is a 64-bit architecture"""
        if "64" in self.desc["proc_arch"]:
            return True
        else:
            return False

    def run_module(self, module_name, args):
	"""Start a module on client"""
	pass
