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
        info("Getting installed apps now...")

        if (self.is_compatible()):
            print "\nInstalled applications:\n==================="

            try:
                if self.client.is_darwin():
                    apps = self.client.conn.modules['os'].listdir('/Applications') #what if I just do a dirwalk in /Apps..???
                    for app in apps:
                        if app.endswith(".app"): # Ignores sub directories; if you comment this out you get subs and files in list
                            try:
                                pl = self.client.conn.modules['plistlib'].readPlist('/Applications/' + app + '/Contents/Info.plist')
                                print app + " " + pl["CFBundleShortVersionString"]
                            except:
                                print app + " No version in plist"
            except Exception as e:
                logger.error(e)
                error(e)

            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
