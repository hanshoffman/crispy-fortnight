import logging

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "ExecuteModule"
class ExecuteModule(CrispyModule):
    """ Execute a binary on a remote machine. """

    compatible_systems = ['all']

    def check_args(self, args):
        self.parser = CrispyArgumentParser(prog="execute", description=self.__doc__)
        self.parser.add_argument("--prog", metavar="<binary_path>", type=str) 
        self.parser.add_argument("--args", metavar="<arguments>", nargs='?', type=str) 

        return self.parser.parse_args(args)

    def run(self, args):
        logger.debug("users run() was called")
        
        try:
            #make sure this is attempting to look in path first
            if not args.args:
                args.args = ""

            if self.client.conn.modules['subprocess'].call([args.prog, args.args]): 
                logger.info("")
                sucess("{} was started successfully.".format("program"))
            else:
                error("{} returned error exit code".format("program"))
        except KeyboardInterrupt:
            logger.info("Caught Ctrl-C")
        except Exception as e:
            logger.error(e)
            error(e)
