.PHONY : default
default : readme.html out.stl

out.stl : cad2stl.py in.igs
	./cad2stl.py in.igs out.stl
	./cad2stl.py --lib /usr/lib/freecad/lib/ in.igs out.stl
	./cad2stl.py -l /usr/lib/freecad/lib/ in.igs out.stl
	-./cad2stl.py --lib /usr/lib/freecad/blah/ in.igs out.stl
	-./cad2stl.py does-not-exist.igs out.stl
	-./cad2stl.py in.igs /blah/out.stl

readme.html : readme.rst
	rst2html readme.rst readme.html

.PHONY : pep8
pep8 : cad2stl.py
	pep8 cad2stl.py

.PHONY : clean
clean :
	rm -f readme.html out.stl
	rm -rf __pycache__/
