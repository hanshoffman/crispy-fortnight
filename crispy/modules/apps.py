import cPickle
import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "AppsModule"
class AppsModule(CrispyModule):
    """ Enum applications on a remote machine. """

    # can be: 'darwin', 'linux', 'windows', 'android'
    compatible_systems = ['darwin']
    
    def marshall_darwin(self):
        import os
        import plistlib

        info = "\n"
        apps = os.listdir('/Applications')
        for app in apps:
            if app.endswith(".app"):
                try:
                    pl = plistlib.readPlist('/Applications/' + app + '/Contents/Info.plist')
                    info += "{} {}\n".format(app[:-4], pl["CFBundleShortVersionString"])
                except:
                    info += "{}\n".format(app[:-4])
        return info

    def marshall_linux(self):
        import os
        #dpkg --get-selections #(Debian)prints WAY too many
        #ls /usr/share/applications/c

    def marshall_windows(self):
        pass

    def run(self, args):
        logger.debug("apps () was called.")
        info("Getting installed apps now...") 
        if (self.is_compatible()):
            try:
                if self.client.is_darwin():
                    data = cPickle.dumps(self.marshall_darwin(), -1)
                if self.client.is_linux():
                    pass
                if self.client.is_windows():
                    pass
                self.client.conn.sendall(data)
                print self.client.conn.recv(1024)
                success("Done.")
            except Exception as e:
                logger.error("{}: {}".format(__class_name__, e))
                error(e)
        else:
            error("OS not implmented yet... help me code it?")
