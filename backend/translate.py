from gcloud_setup import *

"""
Translates given text
"""
def translate(text, lang):
    response = client.translate_text(
        contents = [text],
        target_language_code = lang,
        parent = parent,
    )

    # get translated text
    # for translation in response.translations:
    #     print(translation.translated_text)

    return response.translations[0].translated_text