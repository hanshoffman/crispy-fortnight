import logging
import os

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *

logger = logging.getLogger(__name__)

__class_name__ = "UsersModule"
class UsersModule(CrispyModule):
    """ Enum users on a remote machine. """

    def init_argparse(self):
        self.parser = CrispyArgumentParser(prog="apps", description=self.__doc__)
        #self.parser.add_argument()

    def run(self, args):
        logger.info("in users run()")
