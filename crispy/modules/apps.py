import cPickle
import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "AppsModule"
class AppsModule(CrispyModule):
    """ Enum applications on a remote machine. """

    # can be: 'darwin', 'linux', 'windows', 'android'
    compatible_systems = ['Darwin']
    
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

    def run(self, args):
        logger.debug("apps run() was called.")
        info("Getting installed apps now...") 

        if (self.is_compatible()):
            if self.client.is_darwin():
                data = cPickle.dumps(self.marshall_darwin(), -1)
            elif self.client.is_linux():
                data = cPickle.dumps(self.marshall_linux(), -1) 
            
            try:
                self.client.conn.sendall(data)
                print self.client.conn.recv(1024).rstrip()
            except Exception as e:
                logger.error(e)
                error(e)
            
            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
