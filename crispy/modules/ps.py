import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "PSModule"
class PSModule(CrispyModule):
    """ Get process list on a remote machine. """

    # can be: 'Darwin', 'Linux', 'Windows', 'Android'
    compatible_systems = ['Darwin', 'Linux']

    def run(self, args):
        logger.debug("run(args) was called")

        if (self.is_compatible()):
            spacing = "{:<5}{:<15}"
            print spacing.format("PID", "Name")

            cpid = self.client.conn.modules['os'].getpid()
            try:
#                if self.client.is_darwin():
                    for proc in self.client.conn.modules['psutil'].process_iter():
                        try:
                            pid = proc.as_dict(attrs=['pid', 'name'])
                        except psutil.NoSuchProcess:
                            pass
                        if pid['pid'] == cpid:
                            highlight(spacing.format(pid['pid'], pid['name']), "yellow")
                        else:
                            print spacing.format(pid['pid'], pid['name'])
            except Exception as e:
                logger.error(e)
                error(e)

            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
