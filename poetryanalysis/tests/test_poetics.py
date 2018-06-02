import os
import unittest
import poetryanalysis


class TestPoems(unittest.TestCase):
    def open_poem(self, poem):
        with open(os.path.join('poetryanalysis/poems', poem)) as f:
            return poetryanalysis.tokenize(f.read())

    def test_haiku(self):
        self.assertTrue(poetryanalysis.guess_form(
            self.open_poem('haiku.txt')) == 'haiku')
        self.assertTrue(poetryanalysis.guess_form(
            self.open_poem('tanka.txt')) == 'tanka')

    def test_sonnets(self):
        self.assertTrue(poetryanalysis.guess_form(
            self.open_poem('sonnet.txt')) == 'Shakespearean sonnet')
        self.assertTrue(poetryanalysis.guess_form(self.open_poem(
            'brokensonnet.txt')) == 'sonnet with unusual meter')

    def test_blankverse(self):
        self.assertTrue(poetryanalysis.guess_form(
            self.open_poem('blankverse.txt')) == 'blank verse')

    def test_cinquain(self):
        self.assertTrue(poetryanalysis.guess_form(
            self.open_poem('cinquain.txt')) == 'cinquain')

    def test_ottavarima(self):
        self.assertTrue(poetryanalysis.guess_form(
            self.open_poem('ottavarima.txt')) == 'ottava rima')

    def test_heroiccouplets(self):
        self.assertTrue(poetryanalysis.guess_form(
            self.open_poem('heroiccouplets.txt')) == 'heroic couplets')

    def test_rondeau(self):
        self.assertTrue(poetryanalysis.guess_form(
            self.open_poem('rondeau.txt')) == 'rondeau')

    def test_num_vowels(self):
        self.assertEqual(poetrytools.num_vowels(
            poetrytools.get_syllables('create')[0]),
            2
        )
 
    def test_rhyme_level_1(self):
        self.assertTrue(poetryanalysis.rhymes(
            'berate', 'create', 1))
 
    def test_rhyme_level_2(self):
        self.assertTrue(poetryanalysis.rhymes(
            'junction', 'function', 2))
 
    def test_initial_ryhme(self):
        self.assertTrue(poetryanalysis.rhymes(
            'old', 'cold', 1))

    def test_vowel_index(self):
        self.assertEqual(poetryanalysis.get_nth_last_vowel(
            poetryanalysis.get_syllables('border')[0], 2),
            -2
        )
 
    def test_vowel_index(self):
        self.assertEqual(poetryanalysis.get_nth_last_vowel(
            poetryanalysis.get_syllables('beautiful')[0], 3),
            -6
        )

    def test_vowel_index_tricky(self):
        self.assertEqual(poetryanalysis.get_nth_last_vowel(
            poetryanalysis.get_syllables('ratios')[0], 2),
            -2
        )

    def test_vowel_index_nonexistant(self):
        self.assertIsNone(poetryanalysis.get_nth_last_vowel(
            poetryanalysis.get_syllables('2000')[0], 2)
        )
 
    def test_bad_rhyme_1_syll(self):
        self.assertFalse(poetryanalysis.rhymes(
            'prep', 'stop'))
 
    def test_bad_rhyme_2_syll(self):
        self.assertFalse(poetryanalysis.rhymes(
            'conduct', 'abstract'))

if __name__ == '__main__':
    unittest.main()
