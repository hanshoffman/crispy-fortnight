import logging
import os

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *

logger = logging.getLogger(__name__)

__class_name__ = "AppsModule"
class AppsModule(CrispyModule):
    """ Enum applications on a remote machine. """

    compatible_systems = ['darwin']

    #def init_argparse(self):
    #    self.parser = CrispyArgumentParser(prog="apps", description=self.__doc__)

    def run(self, args):
        logger.info("apps run() was called.")
        print self.client.conn

        #apps = os.listdir('/Applications')
        #for app in apps:
        #    if app[0] == '.':
        #        continue
        #    else:
        #        info += "\t%s\n" %app
        #return info
