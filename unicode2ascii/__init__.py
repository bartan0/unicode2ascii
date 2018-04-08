import re
import unicodedata as ucd

from itertools import count

__version__ = '1.0.1'

# default charmap for asciize()
latin_transliteration = {
	'Æ': 'AE', 'Ð': 'D', 'Þ': 'TH',
	'æ': 'ae', 'ð': 'd', 'þ': 'th', 'ß': 'ss', 'ı': 'i'
}

# pattern the character name must match for "undiacritization" to be possible
_pattern = re.compile('(LATIN (?:CAPITAL|SMALL) LETTER .) WITH .*')

'''Convert string s to its ASCII counterpart (replace letters with diacritics
with their non-diacritized versions).

Let string s consist of ASCII and non-ASCII characters. The resulting string
will then be s with all non-ASCII characters replaced with some strings,
according to replacement rules.

Replacement rules (applied to each character c of string s):
	if c is ASCII character then c is not replaced,
	if c is not ASCII character then:
		if c is one of charmap keys - c is replaced with charmap[c],
		if c is not any of charmap keys - c is replaced with its
		non-diacritized version if possible, if diacritics removing failed, c
		is replaced with replacement character rep.

This function may modify charmap argument.
'''
def asciize(s, rep = '_', charmap = None):
	if charmap == None:
		charmap = latin_transliteration.copy()

	res = list(s)

	for i_c, c in zip(count(0), res):
		if ord(c) <= 127:
			continue

		if ord(c) > 127:
			if c in charmap:
				res[i_c] = charmap[c]
				continue
			else:
				match = re.fullmatch(_pattern, ucd.name(c, ''))
				if match:
					charmap[c] = res[i_c] = ucd.lookup(match.groups()[0])
					continue

		charmap[c] = res[i_c] = rep

	return ''.join(res)
