import re
import unicodedata as ucd

from itertools import count

_asciize_pattern = re.compile('(LATIN (?:CAPITAL|SMALL) LETTER .) WITH .*')

def asciize(s, rep = '_'):
	res = list(s)

	for i_c, c in zip(count(0), res):
		if ord(c) <= 127:
			continue

		if ord(c) > 127:
			match = re.fullmatch(_asciize_pattern, ucd.name(c, ''))
			if match:
				res[i_c] = ucd.lookup(match.groups()[0])
				continue

		res[i_c] = rep

	return ''.join(res)
