import base64
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv() 


def write_file(audio):
    f = open("test.wav", "wb")
    f.write(base64.b64decode(audio))
    f.close()

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

def transcribe(audio):
    write_file(audio)

    #upload file
    headers = {'authorization': os.getenv('API_KEY')} 
    response = requests.post('https://api.assemblyai.com/v2/upload',headers=headers, data=read_file("test.wav"))
    # print(response.json()["upload_url"])

    #transcribe file
    endpoint = "https://api.assemblyai.com/v2/transcript"
    myJson = { "audio_url": response.json()["upload_url"] }
    headers = {
        "authorization": os.getenv('API_KEY'),
        "content-type": "application/json"
    }
    # print(myJson)
    response = requests.post(endpoint, json=myJson, headers=headers)
    print(response.json()['id'])

    # Poll for completion
    while True:
        endpoint = "https://api.assemblyai.com/v2/transcript/"+response.json()['id']
        headers = {
            "authorization": os.getenv('API_KEY'),
        }
        response = requests.get(endpoint, headers=headers)
        status = response.json()['status']
        print(status)
        if(status == 'completed'):
            print(response.json()['text'])
            break
        elif(status == 'error'):
            print(response.json())
            break

    return response.json()['text']

# calls the send_recieve function
# asyncio.get_event_loop().run_until_complete(send_receive())
# currently; websockets allow continuous connection between myself and the server
# what we want: websocket that connects between the front and the back-end; ensure that you can pick up audio (from English to other languages)
# https://websockets.readthedocs.io/en/stable/
# we only want a server 