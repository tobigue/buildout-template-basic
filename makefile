all:
	python bootstrap.py
	bin/buildout

clean:
	rm -rfv bin develop-eggs dist downloads eggs parts
	rm -fv .DS_Store .coverage .installed.cfg
	find . -name '*.pyc' -exec rm -fv {} \;
	find . -name '*.pyo' -exec rm -fv {} \;
	find . -depth -name '*.egg-info' -exec rm -rfv {} \;

name:
	@ echo WARNING: This works only one time, no typos!
	@ echo === What is the project name? ===
	@ read newname ;\
	mv src/projectname src/$$newname ;\
	sed -i s/projectname/$$newname/g buildout.cfg setup.py ;\
	echo === Project $$newname initialized ===
