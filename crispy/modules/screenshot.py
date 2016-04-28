import logging
import os

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "ScreenshotModule"
class ScreenshotModule(CrispyModule):
    """ Take a screenshot of a remote machine. """

    compatible_systems = ['darwin']

    def run(self, args):
        logger.debug("screenshot() was called.")
        info("Capturing screen on client...")
        success("Done. File saved to \'\'")
