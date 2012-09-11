import os
import sys

# env setup

qgis_base = "/Applications/QGIS.app/Contents/Resources/python"
qgis_lib = "/Applications/QGIS.app/Contents/MacOS/lib"

#os.environ['LD_LIBRARY_PATH'] = qgis_lib

sys.path.append(qgis_base)

from qgis.core import *
