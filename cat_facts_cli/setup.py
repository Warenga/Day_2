import sys
from setuptools import setup

setup(
	name='catfacts',
	version='0.1',
	py_modules=['catfacts'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		catfacts=catfacts:main()

	''',
	)