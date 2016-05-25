import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "PSModule"
class PSModule(CrispyModule):
    """ Get process list on a remote machine. """

    compatible_systems = ['all']

    def run(self, args):
        logger.debug("run(args) was called")

        if (self.is_compatible()):
            spacing = "{:<20}{:<6}{:<15}"
            print spacing.format("Username", "PID", "Name")

            cpid = self.client.conn.modules['os'].getpid()
            try:
                for proc in self.client.conn.modules['psutil'].process_iter():
                    try:
                        pid = proc.as_dict(attrs=['username', 'pid', 'name'])
                    except psutil.NoSuchProcess:
                        pass
                    if pid['pid'] == cpid:
                        highlight(spacing.format(pid['username'], pid['pid'], pid['name']), "yellow")
                    else:
                        print spacing.format(pid['username'], pid['pid'], pid['name'])
                success("Done.")
            except KeyboardInterrupt:
                logger.info("Caught Ctrl-C")
            except Exception as e:
                logger.error(e)
                error(e)
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
