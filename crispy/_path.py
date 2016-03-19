import os
import sys

thisdir = os.path.dirname(__file__)
libdir = os.path.join(thisdir, '../relative/path/to/lib/from/bin')

if libdir not in sys.path:
    sys.path.insert(0, libdir)