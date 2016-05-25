import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "CheckAVModule"
class CheckAVModule(CrispyModule):
    """ Determine which (if any) AV is on a remote machine. """

    compatible_systems = ['all']
    
    #https://github.com/rapid7/metasploit-framework/blob/master/data/wordlists/av_hips_executables.txt
    adaware = {'name':'Ad Aware', 'binaries':['Ad-Aware.exe'], 'procs':[]}
    avast = {'name':'Avast', 'binaries':['test'], 'procs':[]} #windows, darwin, android, ios
    avg = {'name':'AVG', 'binaries':['test'], 'procs':[]}
    bitdefender = {'name':'BitDefender', 'binaries':['test'], 'procs':[]}
    comodo = {'name':'Comodo', 'binaries':['test'], 'procs':[]}
    malwarebytes = {'name':'Malware Bytes', 'binaries':['test'], 'procs':[]}
    panda = {'name':'Panda Cloud', 'binaries':['test'], 'procs':[]}
    sophos = {'name':'Sophos AV', 
            'binaries':['/usr/local/bin/sweep'], 
            'procs':['SophosScanD', 'SophosWebIntelligence']}
    zonealarm = {'name':'Zone Alarm', 'binaries':['zonealarm.exe', 'zapro.exe'], 'procs':[]} #add registry keys?
    av_list = [adaware, avast, avg, bitdefender, comodo, malwarebytes, panda, sophos, zonealarm]

    def run(self, args):
	logger.debug("run(args) was called.")
        
        if self.client.conn.modules['os'].geteuid() != 0:
            error("psutil requires this module to be run with root privileges")
            return
        else:
            info("Running through av list now...")
            try:
                for proc in self.client.conn.modules['psutil'].process_iter():
                    try:
                        pid = proc.as_dict(attrs=['username', 'pid', 'name'])
                    except psutil.NoSuchProcess:
                        pass

                    for av in self.av_list:
                        for p in av['procs']:
                            try:
                                if p == proc.name():
                                    warning("Found {} w/ PID {}".format(av['name'], pid['pid']))
                                    return
                            except:
                                pass
                success("Done.")
            except KeyboardInterrupt:
                logger.info("Caught Ctrl-C")
            except Exception as e:
                logger.error(e)
                error(e)
