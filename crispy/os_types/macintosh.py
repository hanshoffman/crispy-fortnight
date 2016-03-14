import datetime
import os
import platform
import subprocess

def enum_os():
    info = "[*] Operating System Info:\n"
    info += "\tComputer Name: %s\n" %platform.node()
    info += "\tModel: %s" %subprocess.check_output(['sysctl', 'hw.model'])[10:]
    info += "\tKernel Version: %s %s\n" %(platform.system(), platform.release())
    info += "\tSystem Date: %s\n" %datetime.datetime.now()
    info += "\tUptime: %s\n" %convert_uptime(subprocess.check_output(['uptime']))
    info += "\tProcessor Type: %s\n" %platform.processor()
    info += "\tCPU Architecture: %s\n" %platform.machine()
    info += "\t# of CPU cores: %s" %subprocess.check_output(['sysctl', 'hw.ncpu'])[9:]
    info += "\tCurrent User: %s\n" %os.getenv('USER')
    info += "\tPATH: %s\n" %os.getenv('PATH')
    info += "\tHOME: %s\n" %os.getenv('HOME')
    info += "\tSHELL: %s\n" %os.getenv('SHELL')
    
    return info

def convert_uptime(s):
    return s[s.find('up')+3:s.find(',')]
    
def enum_interfaces():
    info = "[*] Network Interface[s]:\n"
    
    return info
    #getifaddrs

def enum_users():
    info = "[*] Users:\n"
    
    users = subprocess.check_output(['dscl', '.', '-ls', '/Users'])
    for user in users:
        if user[0] != '_':
            info += "\t%s" %user
    
    return info

def enum_applications():
    info = "[*] Installed Applications:\n"

    apps = os.listdir('/Applications')
    for app in apps:
        if app[0] == '.':
            continue
        else:
            info += "\t%s\n" %app
  
    return info
    
def enum_drives():
    info = "[*] Disk Partitions:\n"
    
    partitions = os.listdir('/Volumes')
    for disk in partitions:
        info += "\t%s" %disk
        
    return info
    
def enum_printers():
    info = "[*] Printers:\n"
    
    printers = os.listdir('/private/etc/cups/ppd/')
    for printer in printers:
        info += "\t%s\n" %printer[:-4]

    return info

def enum_usb():
    info = "[*] USBs:\n"
    
    return info
    #system_profiler SPUSBDataType
    #ioreg -p IOUSB -l -w 0 | grep "USB Product Name"
    
def get_reboot_history():
    info = "[*] Reboot History:\n"
    info += "%s" %subprocess.check_output(['last', 'reboot'])
    
    return info

def get_process_list(): #should this be even included? or left to a shell instead?
    info = "[*] Process List:\n"
    info += "%s" %subprocess.check_output(['ps', 'aux'])
    
    return info
    
def get_ssh_keys():
    info = "[*] Searching for ssh keys:\n"
    
    return info
