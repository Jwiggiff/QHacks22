import base64
import json
from google.cloud import translate
from google.oauth2 import service_account
import os
from dotenv import load_dotenv
load_dotenv()

#get api keys
creds_json = base64.b64decode(os.getenv("GOOGLE_CREDENTIALS")).decode("utf-8");
creds_json = json.loads(creds_json);
credentials = service_account.Credentials.from_service_account_info(creds_json)

# access credentials
project_id = creds_json['project_id']
assert project_id
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient(credentials=credentials)