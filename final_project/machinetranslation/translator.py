'''Importando'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


#Traduz do ingles pro frances
def english_to_french(english_text):
    '''
    Traduz do ingles pro frances
    '''
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translation")


#Traduz-do-Frances-para-o-ingles
def french_to_english(french_text):
    '''
    Traduz do Frances para o ingles 
    '''
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")


load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2023-04-02',authenticator=authenticator)

language_translator.set_service_url(url)
