import unittest
from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # test when Hello is given as input the output is Bonjour
        
        self.assertNotEqual(english_to_french('Bad'), 'Bien')
        #test when Bad is given as input the output is not Bien

class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # test when Bonjour is given as input the output is Hello.

        self.assertNotEqual(french_to_english('Oui'), 'No')
        #test when Oui is given as input the output is not No.

unittest.main()
