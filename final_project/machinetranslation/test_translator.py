import unittest
from translator import french_to_english, english_to_french

class TestfrenchToEnglish(unittest.TestCase):
    '''
    Teste de Frances para Ingles
    '''
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')


class TestEnglishToFrench(unittest.TestCase):
    '''
    Teste de Ingles para Frances
    '''
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')


unittest.main()
