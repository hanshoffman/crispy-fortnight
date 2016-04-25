import logging
import os

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *

logger = logging.getLogger(__name__)

__class_name__ = "CheckAVModule"
class CheckAVModule(CrispyModule):
    """ Determine if and which (if any) AV is on a remote machine. """

    def init_argparse(self):
        self.parser = CrispyArgumentParser(prog="checkav", description=self.__doc__)
        #self.parser.add_argument()

    def run(self, args):
	pass

#determine which av product (if any) is installed. if calculated probability is not 95% or more, then output possible top 3. check for known folders and files. either store in this file as list of dictionaries or store in a file on HDD and read it. 
