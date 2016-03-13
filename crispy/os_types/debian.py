#Ubuntu
#https://docs.python.org/2/library/platform.html
from os_types.base import OperatingSystem

class Debian(OperatingSystem):
    def lp(self):
        print "test"