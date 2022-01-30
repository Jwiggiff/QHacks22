import requests
import os
from dotenv import load_dotenv
load_dotenv() 


def transcribe_a(audio):
    print(audio)
    json = "{'audio_data': '"+audio+"'"
    headers = {'authorization': os.getenv('API_KEY')} 
    response = requests.post('https://api.assemblyai.com/v2/stream',headers=headers, json=json)
    print(response.json())
    return response.json()

def transcribe(audio):
    headers = {'authorization': os.getenv('API_KEY')} 
    response = requests.post('https://api.assemblyai.com/v2/upload',headers=headers, data=audio)
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = response.json()
    headers = {
        "authorization": os.getenv('API_KEY'),
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    print(response.json())
    return response.json()

# calls the send_recieve function
# asyncio.get_event_loop().run_until_complete(send_receive())
# currently; websockets allow continuous connection between myself and the server
# what we want: websocket that connects between the front and the back-end; ensure that you can pick up audio (from English to other languages)
# https://websockets.readthedocs.io/en/stable/
# we only want a server 