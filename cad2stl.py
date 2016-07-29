#! /usr/bin/env python2

import sys

required_args = 2
if len(sys.argv) == required_args + 1:
    in_path  = sys.argv[1]
    out_path = sys.argv[2]
else:
    sys.stderr.write("Usage: {} /path/to/input /path/to/output\n".format(sys.argv[0]))
    sys.exit(1)

sys.path.append('/usr/lib/freecad/lib')
import FreeCAD, Part

in_part = Part.read(in_path)
in_part.exportStl(out_path)
