import cPickle
import logging

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "SearchModule"
class SearchModule(CrispyModule):
    """ Search for a file/files on a remote machine. """

    compatible_systems = ['all']
    
    def init_argparse(self):
        self.parser = CrispyArgumentParser(prog="search", description=self.__doc__)
        #self.parser.add_argument()

    def run(self, args):
        pass        
