"""This Programme aim To Test The Translator Created in translator.py"""
import unittest
from translator import english_to_french,french_to_english

class TestTranslator(unittest.TestCase):
    """This class aime to Test The Translator"""
    def test_equal_english_to_french(self):
        """This Function Test English To French Translator :the result should match the value specified """
        self.assertEqual(english_to_french("Hello"),"Bonjour")
    def test_notequal_english_to_french(self):
        """"This Function Test English To French Translator the result should not match the value specified"""
        self.assertNotEqual(english_to_french("Today"),"Demain")

    def test_equal_french_to_english(self):
        """This Function Test French To English Translator :the result should match the value specified """
        self.assertEqual(french_to_english("Bonjour"),"Hello")
    
    def test_notequal_french_to_english(self):
        """"This Function Test French To English Translator the result should not match the value specified"""
        self.assertNotEqual(french_to_english("Demain"),"Today")

if __name__ == '__main__':
    unittest.main()
