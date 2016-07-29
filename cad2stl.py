#! /usr/bin/env python2

import sys
import os

required_args = 2
if len(sys.argv) == required_args + 1:
    in_path  = sys.argv[1]
    out_path = sys.argv[2]
else:
    sys.stderr.write("Usage: {} /path/to/input /path/to/output\n".format(sys.argv[0]))
    sys.exit(1)

if not os.path.isfile(in_path):
    sys.stderr.write("Error: input is not a file: {}\n".format(in_path))
    sys.exit(1)

if os.path.isabs(out_path):
    out_dir = os.path.dirname(out_path)
    if not os.path.isdir(out_dir):
        sys.stderr.write("Error: output directory does not exist: {}\n".format(out_dir))
        sys.exit(1)

sys.path.append('/usr/lib/freecad/lib')
import FreeCAD, Part

in_part = Part.read(in_path)
in_part.exportStl(out_path)
