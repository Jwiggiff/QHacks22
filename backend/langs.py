from gcloud_setup import *

"""
Returns a list of languages supported by Google Translate
"""
def getLangs():
    # get api response
    response = client.get_supported_languages(parent=parent, display_language_code="en")
    languages = response.languages
    return languages