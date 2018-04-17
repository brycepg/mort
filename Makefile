clean:
	rm -r *.egg-info dist build

build:
	python setup.py bdist_wheel

upload:
	twine upload dist/*
