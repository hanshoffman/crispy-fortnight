import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "UsersModule"
class UsersModule(CrispyModule):
    """ Enum users on a remote machine. """

    # can be: 'darwin', 'linux', 'windows', 'android'
    compatible_systems = ['Darwin', 'Linux']

    def run(self, args):
        logger.debug("users run() was called")
        info("Getting system users now...")

        if (self.is_compatible()):
            print "\nSystem Users:\n==================="
            try:
                if self.client.is_darwin():
                    users = self.client.conn.modules['os'].listdir('/Users')
                elif self.client.is_linux():
                    users = self.client.conn.modules['os'].listdir('/home')

                for u in users:
                    print "{}\n".format(u)
            except Exception as e:
                logger.error(e)
                error(e)
            
            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
