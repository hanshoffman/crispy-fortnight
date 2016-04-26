import logging

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "DrivesModule"
class DrivesModule(CrispyModule):
    """ Enumerate the HDD's on a remote machine. """
    
    def init_argparse(self):
	self.parser = CrispyArgumentParser(prog="drives", description=self.__doc__)
	#self.parser.add_argument()

    def marshall_me(self):
        import os

        partitions = os.listdir('/Volumes')
        
        info = ""
        for disk in partitions:
            info += "\t%s" %disk
        return info + "\n"

    def run(self, args):
	logger.debug("in module.py run()")
	info("Getting Disk Partitions now...\n")
        
        try:
            self.marshall_me()
            success("Done.")
        except Exception as e:
            error(e)
