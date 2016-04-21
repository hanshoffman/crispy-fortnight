import os

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *

logger = logging.getLogger(__name__)

__class_name__ = "AppsModule"
class AppsModule(CrispyModule):
    """ Enum applications on a remote machine. """

    #def init_argparse(self):
    #    self.parser = CrispyArgumentParser(prog="apps", description=self.__doc__)

    def run(self, args):
        logger.info("apps run() was called.")
	print "winning!"
