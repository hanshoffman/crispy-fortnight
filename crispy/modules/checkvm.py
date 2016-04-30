import cPickle
import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "VirtualMachineModule"
class VirtualMachineModule(CrispyModule):
    """ Determine if remote machine is a virtual machine. """

    compatible_systems = ['all']

    def marshall_me(self):
        import os
        signatures = ['virtualbox']

        #check to see if files exist for each product
        #look at which files are installed for each to be more accurate

    def run(self, args):
        try:
            logger.info("VirtualModule() run")
            info("Checking if system is a virtual instance...")
            data = cPickle.dumps(self.marshall_me(), -1)
            self.conn.sendall(data)
            print self.client.conn.recv(1024)
            success("Done.")
        except:
            error("cPickle error.")
