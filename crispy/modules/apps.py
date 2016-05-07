import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "AppsModule"
class AppsModule(CrispyModule):
    """ Enum applications on a remote machine. """

    # can be: 'Darwin', 'Linux', 'Windows', 'Android'
    compatible_systems = ['Darwin']

    def run(self, args):
        logger.debug("run(args) was called")

        if (self.is_compatible()):
            print "\nInstalled applications:\n==================="

            try:
                if self.client.is_darwin():
                    apps = self.client.conn.modules['os'].listdir('/Applications') 
                    for app in apps:
                        if app.endswith(".app"): 
                            try:
                                pl = self.client.conn.modules['plistlib'].readPlist('/Applications/' + app + '/Contents/Info.plist')
                                print app[:-4] + " " + pl["CFBundleShortVersionString"]
                            except:
                                print app[:-4] + " [No version in plist]"
            except Exception as e:
                logger.error(e)
                error(e)

            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
