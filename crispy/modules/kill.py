import logging

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "KillModule"
class KillModule(CrispyModule):
    """ Get process list on a remote machine. """

    compatible_systems = ['all']

    def check_args(self, args):
        self.parser = CrispyArgumentParser(prog="kill", description=self.__doc__)
        self.parser.add_argument("--pid", metavar="<pid>", type=int)

        return self.parser.parse_args(args)

    def run(self, args):
        logger.debug("run(args) was called")

        try:
            self.client.conn.modules['os'].kill(args.pid, 9)
            success("Done.")
        except Exception as e:
            logger.error(e)
            error(e)
