import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

# ------ Authentication ---------------#
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)
language_translator.set_service_url(url)
# ------ Authentication ---------------#

def english_to_french(english_text):
    """"""
    if english_text is (None or ""):
        return ""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return translation["translations"][0]["translation"]

def french_to_english(french_text):
    """"""
    if french_text is (None or ""):
        return ""
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return translation["translations"][0]["translation"]
