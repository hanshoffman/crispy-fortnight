import cPickle
import logging

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "UsersModule"
class UsersModule(CrispyModule):
    """ Enum users on a remote machine. """

    # can be: 'darwin', 'nt', 'android'
    compatible_systems = ['darwin']
    
    #def init_argparse(self):
    #    self.parser = CrispyArgumentParser(prog="apps", description=self.__doc__)
    #    #self.parser.add_argument()

    def marshall_me(self):
        import os 
       
        ignore = ['.localized', 'Guest', 'Shared']
        info = ""
        users = os.listdir('/Users')
        for user in users:
            if user not in ignore:
                info += "{}\n".format(user)
        return info

    def run(self, args):
        logger.debug("in users run()")
        info("Getting system users now...")
        if (self.is_compatible()):
            try:
                data = cPickle.dumps(self.marshall_me(), -1)
                self.client.conn.sendall(data)
                print self.client.conn.recv(1024)
                success("Done.")
            except Exception as e:
                logger.error("{}: {}".format(__class_name__, e))
                error(e)
        else:
            error("OS not implmented yet... help me code it?")
