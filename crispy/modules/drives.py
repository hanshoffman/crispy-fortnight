import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "DrivesModule"
class DrivesModule(CrispyModule):
    """ Enumerate all mounted disk partitions on a remote machine. """
    
    compatible_systems = ['all']

    def bytes2human(self, n):
        symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
        prefix = {}
        
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = float(n) / prefix[s]
                return '%.1f%s' % (value, s)
        
        return "%sB" % n

    #https://github.com/giampaolo/psutil/blob/master/scripts/disk_usage.py (use this code!)
    def run(self, args):
	logger.debug("run(args) was called")
        
        spacing = "{:15}{:12}{:12}{:12}{:<12}{:12}{:12}"
        print spacing.format("Device", "Total", "Used", "Free", "% Used", "Type", "Mount")
        try:
            for part in self.client.conn.modules['psutil'].disk_partitions():
                if self.client.is_windows():
                    if 'cdrom' in part.opts or part.fstype == '':
                        continue
                usage = self.client.conn.modules['psutil'].disk_usage(part.mountpoint)
                print spacing.format(part.device, self.bytes2human(usage.total), self.bytes2human(usage.used), self.bytes2human(usage.free), int(usage.percent), part.fstype, part.mountpoint)
            success("Done.")
        except KeyboardInterrupt:
            logger.info("Caught Ctrl-C")
        except Exception as e:
            logger.error(e)
            error(e)
