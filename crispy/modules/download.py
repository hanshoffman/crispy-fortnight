import logging
import os

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *

logger = logging.getLogger(__name__)

__class_name__ = "DownloadModule"
class DownloadModule(CrispyModule):
    """ Download file from remote machine. """

    def init_argparse(self):
        self.parser = CrispyArgumentParser(prog="download", description=self.__doc__)
	self.parser.add_argument("local_file", metavar="<local_path>", nargs="?", type=str)
        self.parser.add_argument("remote_file", metavar="<remote_path>", required=True, type=str)

    def run(self, args):
	remote_file = "file.jpg"
	
	try:
	    #self.format_info("Attempting download of %s ..." %remote_file) #how can I call format_* from here??
	    logger.info("Download file now...")
	    #self.format_success("File transfer complete.")
	    logger.info("File transfer complete.")
	except:
	    #self.format_error("File transfer failed.")
	    logger.error("File transfer failed.")
