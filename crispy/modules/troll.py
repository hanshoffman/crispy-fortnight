import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "TrollModule"
class TrollModule(CrispyModule):
    """ Troll the victim. """

    compatible_systems = ['Windows']

    def run(self, args):
        logger.debug("troll run() was called")

        if self.is_compatible():
            info("Playing the empiral death march :)")

            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
