import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "NetstatModule"
class NetstatModule(CrispyModule):
    """ Display netstat info on a remote machine. """
    
    compatible_systems = ['all']

    def run(self, args):
	logger.debug("run(args) was called")
       
        #copy this script below!! 
        #https://github.com/giampaolo/psutil/blob/master/scripts/netstat.py
        try:
            success("Done.")
        except Exception as e:
            logger.error(e)
            error(e)
