import platform
import datetime
import os
import subprocess
import socket
import sys

from os import listdir

def enum_os():
    info = "[*] Operating System Info:\n"
    info += "\tComputer Name: %s\n" %platform.node()
    info += "\tKernel Version: %s %s\n" %(platform.system(), platform.release())
    info += "\tSystem Date: %s\n" %datetime.datetime.now()
    info += "\tUptime: %s\n" %subprocess.call(["uptime"])
    info += "\tProcessor Type: %s\n" %platform.processor()
    info += "\tCPU Architecture: %s\n" %platform.machine()
    info += "\tPATH: %s\n" %os.getenv('PATH')
    info += "\tCurrent User %s\n" %os.getenv('USER')
    info += "\tHOME: %s\n" %os.getenv('HOME')
    info += "\tSHELL: %s\n\n" %os.getenv('SHELL')
    return info
    
def enum_interfaces():
    info = "[*] Network Interface[s]:\n"
    return info
    #getifaddrs

def enum_users():
    info = "[*] Users:\n"
    return info
    #dscl . -ls /Users
    #http://superuser.com/questions/592921/mac-osx-users-vs-dscl-command-to-list-user/621055
    #create a hash set of ls /Users/ and dscl . -ls /Users leaving only unique users. then run commands
    #from link above on those users

def enum_applications():
    info = "[*] Installed Applications:\n"
    apps = listdir('/Applications')
    for app in apps:
        if app[0] == '.':
            continue
        else:
            info += "\t%s\n" %app
  
    return info
    
def enum_drives():
    info = "[*] Disk Partitions:\n"
    
    partitions = listdir('/Volumes')
    for disk in partitions:
        info += "\t%s" %disk
        
    return info
    
def enum_printers():
    info = "[*] Printers:\n"
    
    printers = listdir('/private/etc/cups/ppd/')
    for printer in printers:
        info += "\t%s\n" %printer[:-4]
    #ls -al /Library/Printers
    #lpinfo -m
    return info

def enum_usb():
    info = "[*] USBs:\n"
    return info
    #system_profiler SPUSBDataType
    #ioreg -p IOUSB -l -w 0 | grep "USB Product Name"
    
def get_reboot_history():
    info = "[*] Reboot History:\n"
    info += "%s\n" %subprocess.call(["last", "reboot"])
    return info

def get_process_list():
    info = "[*] Process List:\n"
    info += "%s\n" %subprocess.call(["ps", "aux"])
    return info
    
def get_ssh_keys():
    info = "[*] Searching for ssh keys:\n"
    return info
