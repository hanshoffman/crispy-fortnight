import logging

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "SearchModule"
class SearchModule(CrispyModule):
    """ Search for a file/files on a remote machine. """

    compatible_systems = ['Darwin']
    
    def check_args(self, args):
        self.parser = CrispyArgumentParser(prog="search", description=self.__doc__)
        self.parser.add_argument("--path", metavar="<path>", help="starting path", required=True, type=str)
        self.parser.add_argument("--ext", metavar="<extension>", help="ie. pdf, txt, zip", required=True, type=str)
        self.parser.add_argument("search_blob", metavar="<search_blob>", type=str)

        return self.parser.parse_args(args)

    def run(self, args):
        logger.debug("run(args) was called")
        info("Searching for files...")

        try:
            for path, dirs, files in self.client.conn.modules['os'].walk(args.path):
                for name in files:
                    if args.search_blob: #have to include stuff like *name or *name*
                        pass
                    if name.endswith(args.ext):
                        print "{}/{}".format(self.client.conn.modules['os'].path.realpath(path), name)
            success("Done.")
        except Exception as e:
            error(e)
            logger.error(e)
