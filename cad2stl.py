#! /usr/bin/env python2

import sys
import os

def convert(in_file, out_file, lib_dir = None):

    if not os.path.isfile(in_file):
        sys.stderr.write("Error: input is not a file: {}\n".format(in_file))
        sys.exit(1)

    if os.path.isabs(out_file):
        out_dir = os.path.dirname(out_file)
        if not os.path.isdir(out_dir):
            sys.stderr.write("Error: output directory does not exist: {}\n".format(out_dir))
            sys.exit(1)

    if lib_dir:
        if os.path.isdir(lib_dir):
            sys.path.append(lib_dir)
        else:
            sys.stderr.write("Error: FreeCAD lib directory does not exist: {}\n".format(args.lib))
            sys.exit(1)

    try:
        import FreeCAD
    except ImportError:
        if os.name == 'posix':
            libpath = '/usr/lib/freecad/lib'
            if os.path.isdir(libpath):
                sys.path.append(libpath)
            else:
                sys.stderr.write("Cannot find path to FreeCad.so")
                sys.exit(1)
        elif os.name == 'nt':
                sys.stderr.write("Cannot find path to FreeCad.pyd\n")
                sys.stderr.write("Add FreeCAD 'lib' folder to PYTHONPATH\n")
                sys.stderr.write("Example directory: C:\\Program Files\\FreeCAD 0.16\\lib\n")
                sys.exit(1)
        else:
            sys.stderr.write("Error: Unknown OS: {}".format(os.name))
            sys.exit(1)

    import FreeCAD
    import Part

    in_part = Part.read(args.in_file)
    in_part.exportStl(args.out_file)

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description='convert CAD formats to STL format'
    )

    parser.add_argument(
        'in_file',
        help='path to CAD file input'
    )
    parser.add_argument(
        'out_file',
        help='path to STL file output'
    )
    parser.add_argument(
        '-l',
        '--lib',
        help='path to FreeCAD lib directory',
    )

    args = parser.parse_args()

    convert(args.in_file, args.out_file, args.lib)
