import cPickle
import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "UsersModule"
class UsersModule(CrispyModule):
    """ Enum users on a remote machine. """

    # can be: 'darwin', 'linux', 'windows', 'android'
    compatible_systems = ['Darwin', 'Linux']

    def marshall_darwin(self):
        import os 
       
        ignore = ['.localized', 'Guest', 'Shared']
        info = ""
        users = os.listdir('/Users')
        for user in users:
            if user not in ignore:
                info += "{}\n".format(user)
        return info

    def marshall_linux(self):
        import os
        import subprocess

        info = ""
        users = os.listdir('/home')
        for user in users:
            info += user
        #users = subprocess.check_call(['cat', '/etc/passwd'])
        return info

    def run(self, args):
        logger.debug("users run() was called")
        info("Getting system users now...")

        if (self.is_compatible()):
            try:
                if self.client.is_darwin():
                    self.client.conn.sendall(cPickle.dumps(self.marshall_darwin(), -1))
                elif self.client.is_linux():
                    self.client.conn.sendall(cPickle.dumps(self.marshall_linux(), -1))
            
                print self.client.conn.recv(1024).rstrip()
            except Exception as e:
                logger.error(e)
                error(e)
            
            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
