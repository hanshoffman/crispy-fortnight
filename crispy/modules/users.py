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
        
        #https://docs.python.org/2/library/grp.html
        #https://docs.python.org/2/library/pwd.html#module-pwd
        #http://stackoverflow.com/questions/421618/python-script-to-list-users-and-groups
        #format like drives.py
        if (self.is_compatible()):
            spacing = "%-15s %-20s %8s %8s %15s %10s"
            print spacing % (("\nUsername", "Full Name", "UID", "GID", "Home", "Shell"))
            
            try:
                if self.client.is_darwin():
                    users = self.client.conn.modules['os'].listdir('/Users')
                    for user in self.client.conn.modules['pwd'].getpwall():
                        #defautl mac osx gid is 20 or "staff" for non-system users
                        if user[2] == 0 or (user[2] > 500 and user[3] == 20):
                            print spacing % (user[0], user[4], user[2], user[3], user[5], user[6])
                            #create a dictionary to keep unique values then print at end to avoid duplicates?
                elif self.client.is_unix():
                    for user in self.client.conn.modules['pwd'].getpwall():
                        #useradd man pages claims that users w/ gid 0-999 are typically reserved for system accounts
                        if user[2] == 0 or (user[2] > 999 and "nologin" not in user[6]):
                            print user
            except Exception as e:
                logger.error(e)
                error(e)
            
            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
