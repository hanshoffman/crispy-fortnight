import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "ExecuteModule"
class ExecuteModule(CrispyModule):
    """ Execute a binary on a remote machine. """

    # can be: 'darwin', 'linux', 'windows', 'android'
    compatible_systems = ['Darwin']

    def check_args(self, args):
        self.parser = CrispyArgumentParser(prog="execute", description=self.__doc__)
        self.parser.add_argument("--b") #run in background? no, just make this automatic...

    def run(self, args):
        logger.debug("users run() was called")
        
        if (self.is_compatible()):
            try:
                if self.client.is_darwin():
                    pass
            except Exception as e:
                logger.error(e)
                error(e)
            
            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
