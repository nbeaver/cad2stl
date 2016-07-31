The core of the code is just::

    import FreeCAD, Part

    in_part = Part.read("in.igs")
    in_part.exportStl("out.stl")
