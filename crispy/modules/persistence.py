import logging

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "PersistenceModule"
class PersistenceModule(CrispyModule):
    """ Make crispy implant persistent on a remote machine. """

    compatible_systems = ['all']

    def check_args(self, args):
        self.parser = CrispyArgumentParser(prog="persistence", description=self.__doc__)
        self.parser.add_argument("--registry", metavar="<registry>", help="use the registry for persistence") 

        return self.parser.parse_args(args)

    def run(self, args):
        # http://www.fuzzysecurity.com/tutorials/19.html
        try:
            pass
        except KeyboardInterrupt:
            logger.info("Caught Ctrl-C")
