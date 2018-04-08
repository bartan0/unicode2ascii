unicode2ascii
=============

Simple Python 3 package to convert unicode strings to ASCII ones.

The aim of this packege is to provide a simple and straightforward way to
convert any string to its "asciized" version - if the source string contained
any characters with diacritics, they will be converted to non-diacritized
characters (eg. 'ć' will be converted to 'c').

Installation
------------

To install this package you can use pip::

	$ pip3 install unicode2ascii

You can install this package from source as well::

	$ tar -xf unicode2ascii-<version>.tar.gz
	$ cd unicode2ascii-<version>
	$ python3 setup.py install [--user]

Usage
-----

Once the package is installed, it can be used just like a regular Python
package::

	>>> import unicode2ascii

This package provides ``latin_transliteration`` dictionary and one function:
``asciize``.

``latin_transliteration``
	During "asciization", for some characters that we would like to be
	transliterated, the diacritics removing will fail and instead of nice
	asciized characters, replacement chars ('_' by default) will be inserted.
	This situation can be avoided by providing information about
	transliteration of these characters (no information has to be provided
	about characters for which diacritics removing would work well).

	``latin_transliteration`` is a dictionary that makes ``asciize`` function
	work as expected for most Latin-based alphabets. It is defined as follows::

		latin_transliteration = {
			'Æ': 'AE', 'Ð': 'D', 'Þ': 'TH',
			'æ': 'ae', 'ð': 'd', 'þ': 'th', 'ß': 'ss', 'ı': 'i'
		}

``asciize(s, rep = '_', charmap = None)``
	Convert string ``s`` to its ASCII counterpart (replace letters with
	diacritics with their non-diacritized versions).

	Let string ``s`` consist of ASCII and non-ASCII characters. The resulting
	string will then be ``s`` with all non-ASCII characters replaced with some
	strings, according to replacement rules.

	Replacement rules (applied to each character ``c`` of string ``s``):

	* if ``c`` is ASCII character then ``c`` is not replaced,
	* if ``c`` is not ASCII character then:
		* if ``c`` is one of ``charmap`` keys - ``c`` is replaced with
		  ``charmap[c]``,
		* if ``c`` is not any of ``charmap`` keys - ``c`` is replaced with its
		  non-diacritized version if possible; if diacritics removing failed,
		  ``c`` is replaced with replacement character ``rep``.

	If ``charmap`` is ``None``, default charmap - ``latin_transliteration`` -
	is used.

	This function may modify ``charmap`` argument.

License
-------

This package is licensed under MIT License. For details, see ``LICENSE`` file.
