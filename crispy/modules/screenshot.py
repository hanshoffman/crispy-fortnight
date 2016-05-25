import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "ScreenshotModule"
class ScreenshotModule(CrispyModule):
    """ Take a screenshot of a remote machine. """

    compatible_systems = ['Darwin']

    def run(self, args):
        logger.debug("run(args) was called")
        info("Capturing screen on client...")
        
        if self.is_android():
            pass
        else:
            pass
        
        success("Done. File saved to \'\'")
