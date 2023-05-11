"""
    Python module to translate english to french and vice-versa
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey="wvZVnnf7tC2zkrzyRgOQMxf670DxdYtOimdruMWjbK07"
url="https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/15950457-9a04-4ae4-9978-02f2a7ad1f83"


language_translator = LanguageTranslatorV3(version='2023-04-16', authenticator=IAMAuthenticator(apikey))
language_translator.set_service_url(url)


def english_to_french(english_text):
    """
        Converts english texts to french
    """
    translations = language_translator.translate(text=english_text, model_id="en-fr").get_result()
    french_text = translations.get("translations")[0].get("translation")
    return french_text

def french_to_english(french_text):
    """
        Converts french texts to english
    """
    translations = language_translator.translate(text=french_text, model_id="fr-en").get_result()
    english_text = translations.get("translations")[0].get("translation")
    return english_text