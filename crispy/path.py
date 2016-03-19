import os
import sys

thisdir = os.path.dirname(__file__)
libdir = os.path.join(thisdir, '/Users/hdot/Documents/Code/crispy-fortnight/')

if libdir not in sys.path:
    sys.path.insert(0, libdir)