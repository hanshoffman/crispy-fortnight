import logging
import os

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *

logger = logging.getLogger(__name__)

__class_name__ = "VirtualModule"
class VirtualMachineModule(CrispyModule):
    """ Determine if remote machine is a virtual machine. """

    def init_argparse(self):
        self.parser = CrispyArgumentParser(prog="virtual", description=self.__doc__)
        #self.parser.add_argument()

    def run(self, args):
        pass
