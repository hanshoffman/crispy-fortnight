import os

from lib.CrispyModule import *

logger = logging.getLogger(__name__)

class DrivesModule(CrispyModule):
    """ A module to enumerate the HDD's on a remote machine. """
    
    def init_argparse(self):
	pass

    def run(self, args):
	logger.debug("in module.py run()")
	info = "[*] Disk Partitions:\n"

        partitions = os.listdir('/Volumes')
        for disk in partitions:
            info += "\t%s" %disk

	logger.debug(info)
        return info + "\n"
