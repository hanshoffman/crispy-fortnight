import os

from .. lib.myparser import CrispyArgumentParser
from .. lib.module import CrispyModule

logger = logging.getLogger(__name__)

class ScreenshotModule(CrispyModule):
    """ Determine if and which (if any) AV is on a remote machine. """

    def init_argparse(self):
        self.parser = CrispyArgumentParser(prog="screenshot", description=self.__doc__)
        #self.parser.add_argument()

    def run(self, args):
        pass
