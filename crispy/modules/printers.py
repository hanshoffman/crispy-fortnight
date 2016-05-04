import logging

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "PrintersModule"
class PrintersModule(CrispyModule):
    """ Enum printers on a remote machine. """

    # can be: 'Darwin', 'Windows', 'Linux', 'Android'
    compatible_systems = ['Darwin']

    def run(self, args):
        logger.debug("apps () was called.")
        info("Getting installed printers now...")

        if (self.is_compatible()):
            print "\nInstalled printers:\n==================="
            try:
                if self.client.is_darwin():
                    printers = self.client.conn.modules['os'].listdir('/private/etc/cups/ppd/')    
                    for p in printers:
                        print "{}\n".format(p[:-4])
                success("Done.")
            except Exception as e:
                logger.error("{}: {}".format(__class_name__, e))
                error(e)
        else:
            error("OS not implmented yet... help me code it?")
