import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "KillModule"
class KillModule(CrispyModule):
    """ Get process list on a remote machine. """

    compatible_systems = ['all']

    def run(self, args):
        logger.debug("run(args) was called")

        success("Done.")
