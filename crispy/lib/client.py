import fprint
import logging

logger = logging.getLogger(__name__)

class CrispyClient(object):
    """ An object that represents a connection from an implant. """
    
    def __init__(self, desc):
        self.desc = desc
        self.conn = self.desc['conn']

    def __str__(self):
        """ Return string represention"""
        logger.debug("__str__() was called")
	
        return "CrispyClient(id={}, ip={}, macaddr={}, hostname={}, platform={}, proc_type={}, proc_arch={}, uptime={}, date={}, user={}, home={}, shell={})".format(
		self.desc['id'], self.desc['ip'], self.desc['macaddr'], self.desc['hostname'], self.desc['plat'], self.desc['proc_type'], 
		self.desc['proc_arch'], self.desc['uptime'], self.desc['date'], self.desc['user'], self.desc['home'], self.desc['shell'])

    def get_session(self):
        """" Return socket for this CirspyClient object. """
        logger.debug("get_session() was called")
        
        return self.conn

    def get_id(self):
        """ Return id for this CirspyClient object. """
        logger.debug("get_id() was called")
        
        return self.desc['id']

    def short_name(self):
        """ Return string representing a CrispyConnection object (short). """
        logger.debug("short_name() was called")
        
        return "CrispyClient(id={}, user={}, platform={}, hostname={}, ip={})".format(self.desc["id"], self.desc["user"], self.desc["plat"], self.desc["hostname"], self.desc["ip"]) 

    def is_android(self):
        """ Determine if platform connected is an Android device. """
        logger.debug("is_android() was called")
        
        if 'Android' in self.desc['plat']:
            return True
        else:
            return False
    
    def is_darwin(self):
        """ Determine if platform connected is a Macintosh system. """
        logger.debug("is_darwin() was called")
	
        if 'Darwin' in self.desc['plat']:
            return True
        else:
            return False
    
    def is_linux(self):
        """ Determine if platform connected is an Linux system. """
        logger.debug("is_linux() was called")
	
        if 'Linux' in self.desc['plat']:
            return True
        else:
            return False
    
    def is_windows(self):
        """ Determine if platform connected is a Windows system. """
        logger.debug("is_windows() was called")
	
        if 'Windows' in self.desc['plat']:
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
	
        if '64' in self.desc['proc_arch']:
            return True
        else:
            return False

    def run_module(self, module, args):
        """ Start a module on client. """
        logger.debug("run_module() was called")
        
        try:
            module.run(args)
        except Exception as e:
            fprint.error("{}".format(e))
