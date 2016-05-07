import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "ProcessModule"
class ProcessModule(CrispyModule):
    """ Get process on a remote machine. """

    # can be: 'Darwin', 'Linux', 'Windows', 'Android'
    compatible_systems = ['all']

    def run(self, args):
        logger.debug("run(args) was called")
        info("Getting process id now...")

        if (self.is_compatible()):
            print "\nCurrent PID\n==================="

            try:
#                if self.client.is_darwin():
                    pid = self.client.conn.modules['os'].getpid()
                    print pid
            except Exception as e:
                logger.error(e)
                error(e)

            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
