import cPickle
import logging
import os

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "DownloadModule"
class DownloadModule(CrispyModule):
    """ Download file from remote machine. """

    compatible_systems = ['all']

    def init_argparse(self, args):
        self.parser = CrispyArgumentParser(prog="download", description=self.__doc__)
	self.parser.add_argument("local_file", metavar="<local_path>", nargs="?", type=str)
        self.parser.add_argument("remote_file", metavar="<remote_path>", type=str)
        
        try:
            pargs = self.parser.parse_args(shlex.split(args))
            print pargs
            return True
        except:
            return False

    def remote_file_check(self, f):
        import os
        
        return "1" if os.path.isfile(f) else "0"

    def run(self, args): #may just have this as a cli.py function?
        if len(args) == 2:
            if os.path.isfile(args[1]):
                warning("\"{}\" already exists locally and will be overwritten. Please re-run the command to continue.".format(args[1]))
            else:
                logger.info("Downloading file now...")
	        info("Attempting download of {}...".format(args[0]))

                data = cPickle.dumps(self.remote_file_check(args[0]), -1)
                self.client.conn.sendall(data)
                if (int(self.client.conn.recv(1024))):
                    print "file exists remotely"
                    #how to send file to me? maybe have client connect to server on new port? don't think this is possible
                    #logger.info("File transfer complete.")
                    #success("File transfer complete.")
                else:
                    error("\"{}\" does not exist remotely.".format(args[0]))
        else:
            print "usage: run download <session id> <path_to_remote_file> <path_to_save_local_file>\n"
