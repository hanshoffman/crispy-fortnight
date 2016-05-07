import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "PSModule"
class PSModule(CrispyModule):
    """ Get process list on a remote machine. """

    # can be: 'Darwin', 'Linux', 'Windows', 'Android'
    compatible_systems = ['all']

    def run(self, args):
        logger.debug("run(args) was called")
        info("Getting process list now...")

        if (self.is_compatible()):
            print "\nCurrent Process List\n==================="

            try:
#                if self.client.is_darwin():
                    for proc in self.client.conn.modules['psutil'].process_iter():
                        try:
                            pids = proc.as_dict(attrs=['pid', 'name'])
                        except psutil.NoSuchProcess:
                            pass
                        else:
                            print(pids)
            except Exception as e:
                logger.error(e)
                error(e)

            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
