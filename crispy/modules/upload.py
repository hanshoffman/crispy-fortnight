import cPickle
import logging
import os

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "UploadModule"
class UploadModule(CrispyModule):
    """ Upload file to remote machine. """

    compatible_systems = ['all']

    def check_args(self, args):
        self.parser = CrispyArgumentParser(prog="run upload", description=self.__doc__)
        self.parser.add_argument("local_file", metavar="<local_path>", type=str)
        self.parser.add_argument("remote_file", metavar="<remote_path>", nargs="?", type=str)
    
        try:
            pargs = self.parser.parse_args(args)
        except Exception as e:
            print e
            return False

        return True

    def remote_file_check(self, f):
        import os

        return "1" if os.path.isfile(f) else "0"

    def run(self, args):
        if os.path.isfile(args[0]):
            try:
                info("Attempting upload of %s ..." %local_file)
                success("File transfer complete.")
                logger.info("File transfer complete.")
            except:
                error("File transfer failed.")
                logger.error("File transfer failed.")
        else:
            error("\"{}\" does not exist locally.".format(args[0]))
