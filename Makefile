.PHONY: test

init:
	pip install --quiet --requirement=requirements.txt
	pip install --quiet --requirement=test-requirements.txt

test:
	flake8 --ignore=E501 ckan_to_spark

publish:
	pip install 'twine>=1.5.0'
	pip install wheel
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg requests.egg-info