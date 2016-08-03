default : readme.html out.stl

out.stl :
	./cad2stl.py in.igs out.stl
	./cad2stl.py --lib /usr/lib/freecad/lib/ in.igs out.stl
	./cad2stl.py -l /usr/lib/freecad/lib/ in.igs out.stl
	-./cad2stl.py --lib /usr/lib/freecad/blah/ in.igs out.stl
	-./cad2stl.py does-not-exist.igs out.stl
	-./cad2stl.py in.igs /blah/out.stl

readme.html : readme.rst
	rst2html readme.rst readme.html
