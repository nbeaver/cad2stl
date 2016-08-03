#! /usr/bin/env python2

def convert(in_file, out_file, lib_dir = None):

    import sys
    import os

    if not os.path.isfile(in_file):
        raise IOError("could not find input file: {}".format(in_file))

    if os.path.isabs(out_file):
        out_dir = os.path.dirname(out_file)
        if not os.path.isdir(out_dir):
            raise IOError("output directory does not exist: {}".format(out_dir))

    if lib_dir:
        if os.path.isdir(lib_dir):
            sys.path.append(lib_dir)
        else:
            raise IOError("FreeCAD lib directory does not exist: {}".format(lib_dir))

    try:
        import FreeCAD
    except ImportError:
        if os.name == 'posix':
            possible_lib_dirs = [
                '/usr/lib/freecad/lib', # Linux
                '/usr/lib64/freecad/lib', # Linux
                '/Applications/FreeCAD.app/Contents/Frameworks/lib', # Mac OS X
            ]
            for lib_dir in possible_lib_dirs:
                if os.path.isdir(lib_dir):
                    sys.path.append(lib_dir)
                    break
            else:
                sys.stderr.write("Cannot find path to FreeCad.so\n")
                raise
        elif os.name == 'nt':
                sys.stderr.write("Cannot find path to FreeCad.pwd\n")
                raise
        else:
            raise NotImplementedError("Unknown OS: {}".format(os.name))

    import FreeCAD # no harm in re-importing
    import Part

    in_part = Part.read(in_file)
    in_part.exportStl(out_file)

def main():
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

if __name__ == '__main__':
    main()
