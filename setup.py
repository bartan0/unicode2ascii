from setuptools import setup

def file_read(fname):
	with open(fname) as f:
		res = f.read()
	return res

setup(
	name = 'unicode2ascii',
	version = '1.0.1',
	license = 'MIT',
	python_requires = '>=3',
	packages = ['unicode2ascii'],
	url = 'https://github.com/bartan0/unicode2ascii',

	author = 'Bartłomiej Sługocki',
	author_email = '0@bartan0.pl',

	description = \
		'Small and simple package to convert Unicode strings' \
		' to their ASCII counterparts.',
	long_description = file_read('README.rst'),
	keywords = 'unicode ascii utf8 utf-8 diacritics string transliteration',
	classifiers = [
		'License :: OSI Approved :: MIT License',
		'Development Status :: 5 - Production/Stable',
		'Programming Language :: Python :: 3 :: Only'
	]
)
