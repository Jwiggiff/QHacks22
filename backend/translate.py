from gcloud_setup import *

"""
Translates text to a specified language

text -- The text to translate
lang -- The language code
"""
def translate(text, lang):
    # get api response
    response = client.translate_text(
        contents = [text],
        target_language_code = lang,
        parent = parent,
    )

    # get translated text
    # for translation in response.translations:
    #     print(translation.translated_text)

    return response.translations[0].translated_text