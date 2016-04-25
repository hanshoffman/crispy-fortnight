import logging
import os

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *

logger = logging.getLogger(__name__)

__class_name__ = "ScreenshotModule"
class ScreenshotModule(CrispyModule):
    """ Determine if and which (if any) AV is on a remote machine. """

    def init_argparse(self):
        self.parser = CrispyArgumentParser(prog="screenshot", description=self.__doc__)
        #self.parser.add_argument()

    def run(self, args):
        pass
