#! /usr/bin/env python2

import sys
sys.path.append('/usr/lib/freecad/lib')
import FreeCAD, Part

required_args = 2
if len(sys.argv) == required_args + 1:
    in_path  = sys.argv[1]
    out_path = sys.argv[2]
else:
    print "{} /path/to/input /path/to/output".format(sys.argv[0])
    sys.exit(1)

in_part = Part.read(in_path)
in_part.exportStl(out_path)
