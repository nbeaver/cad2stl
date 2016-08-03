The core of the code is just this::

    import FreeCAD, Part

    in_part = Part.read("in.igs")
    in_part.exportStl("out.stl")
