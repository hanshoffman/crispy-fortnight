import os

from .. lib.myparser import CrispyArgumentParser
from .. lib.module import CrispyModule

logger = logging.getLogger(__name__)

class PersistenceModule(CrispyModule):
    """ Make crispy implant persistent on a remote machine. """

    def init_argparse(self):
        self.parser = CrispyArgumentParser(prog="persistence", description=self.__doc__)
        #self.parser.add_argument()

    def run(self, args):
        pass
