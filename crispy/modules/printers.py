import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "PrintersModule"
class PrintersModule(CrispyModule):
    """ Enum printers on a remote machine. """

    # can be: 'Darwin', 'Windows', 'Linux', 'Android'
    compatible_systems = ['Darwin', 'Linux']

    def run(self, args):
        logger.debug("apps () was called.")

        if (self.is_compatible()):
            print "\nInstalled printers:\n==================="
            try:
                if self.client.is_darwin():
                    printers = self.client.conn.modules['os'].listdir('/private/etc/cups/ppd/')    
                    for p in printers:
                        print "{}\n".format(p[:-4])
                elif self.client.is_linux():
                    printers = self.client.conn.modules['subprocess'].check_output(['lpstat', 'a'])
                    print printers #stdout is not being tunneled over connection, rather outputing on host
                success("Done.")
            except KeyboardInterrupt:
                logger.info("Caught Ctrl-C")
            except Exception as e:
                logger.error(e)
                error(e)
        else:
            error("OS not implmented yet... help me code it?")
