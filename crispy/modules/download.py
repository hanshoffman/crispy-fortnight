import os

from .. lib.myparser import CrispyArgumentParser
from .. lib.module import CrispyModule

logger = logging.getLogger(__name__)

class DownloadModule(CrispyModule):
    """ Download file from remote machine. """

    def init_argparse(self):
        self.parser = CrispyArgumentParser(prog="download", description=self.__doc__)
	self.parser.add_argument("local_file", metavar="<local_path>", nargs="?", type=str)
        self.parser.add_argument("remote_file", metavar="<remote_path>", required=True, type=str)

    def run(self, args):
	remote_file = "file.jpg"
	
	try:
	    self.format_info("Attempting download of %s ..." %remote_file)
	    print "call to download()"
	    self.format_success("File transfer complete.")
	    logger.info("File transfer complete.")
	except:
	    self.format_error("File transfer failed.")
	    logger.error("File transfer failed.")
