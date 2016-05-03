import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "AppsModule"
class AppsModule(CrispyModule):
    """ Enum applications on a remote machine. """

    # can be: 'Darwin', 'Linux', 'Windows', 'Android'
    compatible_systems = ['Darwin']
    
    def check_args(self, args):
        self.parser = CrispyArgumentParser(prog="download", description=self.__doc__)
        
        return self.parser.parse_args(args)

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

    def run(self, args):
        logger.debug("run(args) was called.")
        info("Getting installed apps now...") 

        if (self.is_compatible()):
            if self.client.is_darwin():
                pass
            elif self.client.is_linux():
                pass
            
            try:
                pass
            except Exception as e:
                logger.error(e)
                error(e)
            
            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
