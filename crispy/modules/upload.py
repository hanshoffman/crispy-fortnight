import logging

from crispy.lib.myparser import CrispyArgumentParser
from rpyc.utils.classic import upload
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "UploadModule"
class UploadModule(CrispyModule):
    """ Upload file to remote machine. """

    compatible_systems = ['all']

    def check_args(self, args):
        self.parser = CrispyArgumentParser(prog="upload", description=self.__doc__)
        self.parser.add_argument("local_file", metavar="<local_file_path>", type=str)
        self.parser.add_argument("remote_file", metavar="<remote_file_path>", type=str)
   
        return self.parser.parse_args(args)

    def run(self, args):
        logger.debug("run(args) was called")
        info("Attempting to upload file...")
       
        try:
            upload(self.client.conn, args.local_file, args.remote_file)
            success("File transfer complete.")
            logger.info("File transfer complete.")
        except ValueError as e:
            error("Cannot upload file")
            logger.error("File transfer failed.")
