import os
import unittest
import translator as t

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

class TestTranslator(unittest.TestCase):
    
    def setUp(self):
        authenticator = IAMAuthenticator(apikey)
        self.language_translator = LanguageTranslatorV3(
            version=version,
            authenticator=authenticator
        )
        self.language_translator.set_service_url(url)

    def test_english_to_french(self):
        empty_text = t.english_to_french("")
        self.assertEqual(empty_text, "")
        simple_text = t.english_to_french("Hello")
        self.assertEqual(simple_text, "Bonjour")

    def test_french_to_english(self):
        empty_text = t.french_to_english("")
        self.assertEqual(empty_text, "")
        simple_text = t.french_to_english("Bonjour")
        self.assertEqual(simple_text, "Hello")

if __name__ == '__main__':
    unittest.main()