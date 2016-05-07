import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "CheckVM"
class CheckVM(CrispyModule):
    """ Determine if remote host is a virtual machine. """

    compatible_systems = ['all']

    signatures = ['virtualbox', 'iprt-VBoxWQueue', 'VBoxService', 'VBoxClient']

    def run(self, args):
        logger.info("VirtualModule() run")
        
        # O(n^2) complexity
        try:
            for proc in self.client.conn.modules['psutil'].process_iter():
                for sig in self.signatures:
                    if sig in proc.name():
                        warning("High probability remote host is a virtual machine.")
                        return
            success("Done.")
        except Exception as e:
            logger.error(e)
            error(e)
