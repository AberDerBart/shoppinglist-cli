from setuptools import setup, find_packages

setup(name='shoppinglist',
	version='0.1',
	description='A command line client for shoppinglist',
	long_description=open('README.md').read(),
	long_description_content_type="text/markdown",
	url='https://github.com/aberderbart/shoppinglist-cli.git',
	author='AberDerBart',
	author_email='nonatz@web.de',
	packages=find_packages(),
	install_requires=[
		'requests',
		'python-Levenshtein',
		'rcfile',
		'uuid',
		'distutils',
	],
	scripts=['bin/shoppinglist'],
	zip_safe=False)
