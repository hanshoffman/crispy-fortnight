import logging
import re

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "SearchModule"
class SearchModule(CrispyModule):
    """ Search for a file/files on a remote machine. """

    compatible_systems = ['all']
    
    def check_args(self, args):
        self.parser = CrispyArgumentParser(prog="search", description=self.__doc__)
        self.parser.add_argument("--path", metavar="<path>", help="starting path", required=True, type=str)
        self.parser.add_argument("--ext", metavar="<extension>", help="ie. pdf, txt, zip", type=str)
        self.parser.add_argument("--keyword", metavar="<keyword>", type=str)

        return self.parser.parse_args(args)

    def run(self, args):
        logger.debug("run(args) was called")
        info("Searching for files...")

        try:
            if not args.ext and not args.keyword:
                raise Exception("must have either --ext or --keyword or both")
            else:
                for (dirpath, dirnames, filenames) in self.client.conn.modules['os'].walk(args.path):
                    for name in filenames:
                        if args.ext: 
                            if name.endswith(args.ext):
                                if args.keyword:
                                    if re.search(args.keyword, name):
                                        print "{}/{}".format(self.client.conn.modules['os'].path.realpath(dirpath), name)
                                else:
                                    print "{}/{}".format(self.client.conn.modules['os'].path.realpath(dirpath), name)
            success("Done.")
        except KeyboardInterrupt:
            logger.info("Caught Ctrl-C")
        except Exception as e:
            error(e)
            logger.error(e)
