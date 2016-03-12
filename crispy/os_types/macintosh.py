import platform
import datetime
import os
import subprocess
import socket
import sys
import array
import struct
import fcntl

from os import listdir

def enum_os():
    print "[*] Operating System Info:"
    print "\tComputer Name:", platform.node()
    print "\tKernel Version:", platform.system(), platform.release()
    print "\tSystem Date:", datetime.datetime.now()
    #print "\tUptime:", subprocess.call(["uptime", "|", "cut", "-d\' \'", "-f2-5"])
    print "\tProcessor Type:", platform.processor()
    print "\tCPU Architecture:", platform.machine()
    print "\tPATH:", os.getenv('PATH')
    print "\tCurrent User:", os.getenv('USER')
    print "\tHOME:", os.getenv('HOME')
    print "\tSHELL:", os.getenv('SHELL')
    print "\n"
    
def enum_interfaces():
    print "[*] Network Interface[s]:"
    #getifaddrs

def enum_users():
    print "[*] Users:"
    #dscl . -ls /Users
    #http://superuser.com/questions/592921/mac-osx-users-vs-dscl-command-to-list-user/621055
    #create a hash set of ls /Users/ and dscl . -ls /Users leaving only unique users. then run commands
    #from link above on those users

def enum_applications():
    print "[*] Installed Applications:"
    apps = listdir('/Applications')
    for app in apps:
        if app[0] == '.':
            continue
        else:
            print "\t", app
    print "\n"
    
def enum_drives():
    print "[*] Disk Partitions:"
    partitions = listdir('/Volumes')
    for disk in partitions:
        print "\t", disk
    print "\n"
    
def enum_printers():
    print "[*] Printers:"
    printers = listdir('/private/etc/cups/ppd/')
    for printer in printers:
        print "\t", printer[:-4]
    print "\n"
    #ls -al /Library/Printers
    #lpinfo -m

def enum_reboot_history():
    print "[*] Reboot History:"
    subprocess.call(["last", "reboot"])

def enum_usb():
    print "[*] USBs:"
    #system_profiler SPUSBDataType
    #ioreg -p IOUSB -l -w 0 | grep "USB Product Name"

def get_process_list():
    print "[*] Process List:"
    subprocess.call(["ps", "aux"])
    print "\n"
    
def get_ssh_keys():
    print "[*] Searching for ssh keys:"
