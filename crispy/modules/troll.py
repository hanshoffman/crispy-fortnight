import logging

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "TrollModule"
class TrollModule(CrispyModule):
    """ Troll the victim. """

    compatible_systems = ['all']

    def check_args(self, args):
        self.parser = CrispyArgumentParser(prog="troll", description=self.__doc__)
        #self.parser.add_argument() 

        return self.parser.parse_args(args)

    def run(self, args):
        pass
