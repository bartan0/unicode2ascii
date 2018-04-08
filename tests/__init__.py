import unittest

from unicode2ascii import asciize

class TestAsciize(unittest.TestCase):
	def test_ascii(self):
		cs = ''.join((chr(i) for i in range(128)))
		self.assertEqual(asciize(cs), cs)

	def test_rep(self):
		self.assertEqual(asciize('λ', '\\'), '\\')

	def test_pangram_en(self):
		self.assertEqual(asciize(
			'A quick brown fox jumps over the lazy dog.'.upper()),
			'A quick brown fox jumps over the lazy dog.'.upper()
		)
		self.assertEqual(asciize(
			'A quick brown fox jumps over the lazy dog.'),
			'A quick brown fox jumps over the lazy dog.'
		)

	def test_pangram_dk(self):
		self.assertEqual(asciize(
			'Masseødelæggelsesvåben'.upper(), charmap = {'Æ': 'AE'}),
			'Masseodelaeggelsesvaben'.upper()
		)
		self.assertEqual(asciize(
			'Masseødelæggelsesvåben', charmap = {'æ': 'ae'}),
			'Masseodelaeggelsesvaben'
		)

	def test_pangram_cz(self):
		self.assertEqual(asciize(
			'Příliš žluťoučký kůň úpěl ďábelské ódy.'.upper()),
			'Prilis zlutoucky kun upel dabelske ody.'.upper()
		)
		self.assertEqual(asciize(
			'Příliš žluťoučký kůň úpěl ďábelské ódy.'),
			'Prilis zlutoucky kun upel dabelske ody.'
		)

	def test_pangram_dk2(self):
		self.assertEqual(asciize(
			'Ærøål'.upper(), charmap = {'Æ': 'AE'}),
			'AEroal'.upper()
		)
		self.assertEqual(asciize(
			'Ærøål', charmap = {}),
			'_roal'
		)

	def test_pangram_fr(self):
		self.assertEqual(asciize(
			'Ça me fait peur de fêter noël là, sur cette île bizarroïde où une mère et sa môme essaient de me tuer avec un gâteau à la cigüe brûlé.'.upper()),
			'Ca me fait peur de feter noel la, sur cette ile bizarroide ou une mere et sa mome essaient de me tuer avec un gateau a la cigue brule.'.upper()
		)
		self.assertEqual(asciize(
			'Ça me fait peur de fêter noël là, sur cette île bizarroïde où une mère et sa môme essaient de me tuer avec un gâteau à la cigüe brûlé.'),
			'Ca me fait peur de feter noel la, sur cette ile bizarroide ou une mere et sa mome essaient de me tuer avec un gateau a la cigue brule.'
		)

	def test_pangram_de(self):
		self.assertEqual(asciize(
			'Heizölrückstoßabdämpfung'.upper()),
			'Heizolruckstossabdampfung'.upper()
		)
		self.assertEqual(asciize(
			'Heizölrückstoßabdämpfung', charmap = {'ß': 'ss'}),
			'Heizolruckstossabdampfung'
		)

	def test_pangram_hu(self):
		self.assertEqual(asciize(
			'árvíztűrő tükörfúrógép'.upper()),
			'arvizturo tukorfurogep'.upper()
		)
		self.assertEqual(asciize(
			'árvíztűrő tükörfúrógép'),
			'arvizturo tukorfurogep'
		)

	def test_pangram_is(self):
		self.assertEqual(asciize(
			'Sævör grét áðan því úlpan var ónýt.'.upper(), charmap = {
				'Æ': 'AE',
				'Ð': 'D',
				'Þ': 'TH'
			}),
			'Saevor gret adan thvi ulpan var onyt.'.upper()
		)
		self.assertEqual(asciize(
			'Sævör grét áðan því úlpan var ónýt.', charmap = {
				'æ': 'ae',
				'ð': 'd',
				'þ': 'th'
			}),
			'Saevor gret adan thvi ulpan var onyt.'
		)

	def test_pangram_no(self):
		self.assertEqual(asciize(
			'Blåbærsyltetøy'.upper(), charmap = {'Æ': 'AE'}),
			'Blabaersyltetoy'.upper()
		)
		self.assertEqual(asciize(
			'Blåbærsyltetøy'),
			'Blabaersyltetoy'
		)

	def test_pangram_pl(self):
		self.assertEqual(asciize(
			'Zażółć gęślą jaźń.'.upper()),
			'Zazolc gesla jazn.'.upper()
		)
		self.assertEqual(asciize(
			'Zażółć gęślą jaźń.'),
			'Zazolc gesla jazn.'
		)

	def test_pangram_tr(self):
		self.assertEqual(asciize(
			'Şişli’de büyük çöp yığınları.'.upper()),
			'Sisli_de buyuk cop yiginlari.'.upper()
		)
		self.assertEqual(asciize(
			'Şişli’de büyük çöp yığınları.', charmap = {'ı': 'i'}),
			'Sisli_de buyuk cop yiginlari.'
		)

	def test_pangram_sk(self):
		self.assertEqual(asciize(
			'Päťtýždňové vĺčatá nervózne štekajú na môjho ďatľa v tŕní.'.upper()),
			'Pattyzdnove vlcata nervozne stekaju na mojho datla v trni.'.upper()
		)
		self.assertEqual(asciize(
			'Päťtýždňové vĺčatá nervózne štekajú na môjho ďatľa v tŕní.'),
			'Pattyzdnove vlcata nervozne stekaju na mojho datla v trni.'
		)

	def test_pangram_se(self):
		self.assertEqual(asciize(
			'Ölälskaråsna'.upper()),
			'Olalskarasna'.upper()
		)
		self.assertEqual(asciize(
			'Ölälskaråsna'),
			'Olalskarasna'
		)

	def test_pangram_ee(self):
		self.assertEqual(asciize(
			'See väike mölder jõuab rongile hüpata.'.upper()),
			'See vaike molder jouab rongile hupata.'.upper()
		)
		self.assertEqual(asciize(
			'See väike mölder jõuab rongile hüpata.'),
			'See vaike molder jouab rongile hupata.'
		)

	def test_pangram_lv(self):
		self.assertEqual(asciize(
			'Sarkanās jūrascūciņas peld pa jūru.'.upper()),
			'Sarkanas jurascucinas peld pa juru.'.upper()
		)
		self.assertEqual(asciize(
			'Sarkanās jūrascūciņas peld pa jūru.'),
			'Sarkanas jurascucinas peld pa juru.'
		)

	def test_pangram_es(self):
		self.assertEqual(asciize(
			'El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja.'.upper()),
			'El veloz murcielago hindu comia feliz cardillo y kiwi. La ciguena tocaba el saxofon detras del palenque de paja.'.upper()
		)
		self.assertEqual(asciize(
			'El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja.'),
			'El veloz murcielago hindu comia feliz cardillo y kiwi. La ciguena tocaba el saxofon detras del palenque de paja.'
		)

	def test_pangram_ru(self):
		self.assertEqual(asciize(
			'Съешь ещё этих мягких французских булок да выпей же чаю.'.upper()),
			'_____ ___ ____ ______ ___________ _____ __ _____ __ ___.'.upper()
		)
		self.assertEqual(asciize(
			'Съешь ещё этих мягких французских булок да выпей же чаю.'),
			'_____ ___ ____ ______ ___________ _____ __ _____ __ ___.'
		)

	def test_pangram_bg(self):
		self.assertEqual(asciize(
			'Под южно дърво, цъфтящо в синьо, бягаше малко пухкаво зайче.'.upper()),
			'___ ____ _____, _______ _ _____, ______ _____ _______ _____.'.upper()
		)
		self.assertEqual(asciize(
			'Под южно дърво, цъфтящо в синьо, бягаше малко пухкаво зайче.'),
			'___ ____ _____, _______ _ _____, ______ _____ _______ _____.'
		)

	def test_pangram_gr(self):
		self.assertEqual(asciize(
			'Ο καλύμνιος σφουγγαράς ψιθύρισε πως θα βουτήξει χωρίς να διστάζει.'.upper()),
			'_ _________ __________ ________ ___ __ ________ _____ __ ________.'.upper()
		)
		self.assertEqual(asciize(
			'Ο καλύμνιος σφουγγαράς ψιθύρισε πως θα βουτήξει χωρίς να διστάζει.'),
			'_ _________ __________ ________ ___ __ ________ _____ __ ________.'
		)

if __name__ == '__main__':
	unittest.main()
