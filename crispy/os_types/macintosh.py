import datetime
import os
import platform
import re
import subprocess

from crispy.os_types.base import Base

class Mac(Base):
    '''Mac OSX'''
    
    def enum_os(self):
        info = "[*] Operating System Info:\n"
        info += "\tComputer Name: {0}\n".format(platform.node())
        info += "\tModel: {0}".format(subprocess.check_output(['sysctl', 'hw.model'])[10:])
        info += "\tKernel Version: {0} {1}\n".format(platform.system(), platform.release())
        info += "\tSystem Date: {0}\n".format(datetime.datetime.now())
        info += "\tUptime: {0} day(s)\n".format(re.findall(r'up ([\d]+)', subprocess.check_output(['uptime']))[0])
        info += "\tProcessor Type: {0}\n".format(platform.processor())
        info += "\tCPU Architecture: {0}\n".format(platform.machine())
        info += "\t# of CPU cores: {0}".format(subprocess.check_output(['sysctl', 'hw.ncpu'])[9:])
        info += "\tCurrent User: {0}\n".format(os.getenv('USER'))
        info += "\tPATH: {0}\n".format(os.getenv('PATH'))
        info += "\tHOME: {0}\n".format(os.getenv('HOME'))
        info += "\tSHELL: {0}\n".format(os.getenv('SHELL'))
        
        return info
    
    def enum_users(self):
        info = "[*] Users:\n"
        
        users = subprocess.check_output(['dscl', '.', '-ls', '/Users'])
        for user in users:
            if user[0] != '_':
                info += "\t%s" %user
        
        return info
    
    def enum_applications(self):
        info = "[*] Installed Applications:\n"
    
        apps = os.listdir('/Applications')
        for app in apps:
            if app[0] == '.':
                continue
            else:
                info += "\t%s\n" %app
      
        return info
        
    def enum_drives(self):
        info = "[*] Disk Partitions:\n"
        
        partitions = os.listdir('/Volumes')
        for disk in partitions:
            info += "\t%s" %disk
            
        return info + "\n"
        
    def enum_printers(self):
        info = "[*] Printers:\n"
        
        printers = os.listdir('/private/etc/cups/ppd/')
        for printer in printers:
            info += "\t%s\n" %printer[:-4]
    
        return info
        
    def get_ssh_keys(self):
        info = "[*] Searching for ssh keys:\n"
        
        users = os.listdir('/Users')
        for user in users:
            if user[0] == '.' or user == 'Guest' or user == 'Shared':
                continue
            else:
                userPath = '/Users/' + user + '/.ssh'
                
                if os.path.isdir(userPath):
                    info += "[+] Found - " + userPath + ":\n"
                    
                files = os.listdir(userPath) 
                for f in files:
                    info += "\t" + f + "\n"
        
        return info