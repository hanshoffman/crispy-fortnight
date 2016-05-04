import logging
import os

from crispy.lib.myparser import CrispyArgumentParser
from rpyc.utils.classic import download
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "DownloadModule"
class DownloadModule(CrispyModule):
    """ Download file from remote machine. """

    compatible_systems = ['all']

    def check_args(self, args):
        self.parser = CrispyArgumentParser(prog="download", description=self.__doc__)
        self.parser.add_argument("remote_file", metavar="<remote_path>", type=str)
	self.parser.add_argument("local_file", metavar="<local_path>", type=str)
        
        return self.parser.parse_args(args) 

    def run(self, args): 
        logger.debug("run(args) was called.")

        if os.path.isfile(args.local_file):
            warning("\"{}\" already exists locally.".format(args.local_file))
        else:
            logger.info("Attempting to download file...")
	    info("Attempting to download file...")
            
            try:
                download(self.client.conn, args.remote_file, args.local_file)
                logger.info("File transfer complete.")
                success("File transfer complete.")
            except ValueError as e:
                error("Cannot download file")
