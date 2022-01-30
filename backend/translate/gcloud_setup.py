from os import environ
from google.cloud import translate

#get api keys
environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

# access credentials
project_id = environ.get("PROJECT_ID", "")
assert project_id
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient()