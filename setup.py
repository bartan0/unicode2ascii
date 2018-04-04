from setuptools import setup

def file_read(fname):
	with open(fname) as f:
		res = f.read()
	return res

setup(
	name = 'unicode2ascii',
	version = '0.1.1',
	license = 'MIT',
	packages = ['unicode2ascii', 'unicode2ascii.tests'],
	url = 'https://github.com/bartan0/unicode2ascii',

	description = \
		'Small and simple package to convert Unicode strings' \
		' to their ASCII counterparts.',
	long_description = file_read('README.md'),
	keywords = 'unicode ascii utf8 utf-8 diacritics string',

	author = 'Bartłomiej Sługocki',
	author_email = '0@bartan0.pl',
)
