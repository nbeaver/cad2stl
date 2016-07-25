#! /usr/bin/env freecadcmd
import Part

import sys
required_args = 3
if len(sys.argv) == required_args + 1:
    in_path  = sys.argv[2]
    out_path = sys.argv[3]
else:
    print sys.argv
    print "{} {} /path/to/input /path/to/output".format(sys.argv[0], sys.argv[1])
    sys.exit(1)

in_part = Part.read(in_path)
in_part.exportStl(out_path)
