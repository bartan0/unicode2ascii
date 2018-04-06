import re
import unicodedata as ucd

from itertools import count

latin_transliteration = {
	'Æ': 'AE', 'Ð': 'D', 'Þ': 'TH',
	'æ': 'ae', 'ð': 'd', 'þ': 'th', 'ß': 'ss', 'ı': 'i'
}

_pattern = re.compile('(LATIN (?:CAPITAL|SMALL) LETTER .) WITH .*')

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
