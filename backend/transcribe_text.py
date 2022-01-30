import base64
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv() 

def write_file(audio):
    """
    This function writes the audio to a new file.
    Parameters: audio - raw audio data from the user on JavaScript
    Return: None
    """

    f = open("test.wav", "wb")
    # write raw audio data to file
    f.write(base64.b64decode(audio))
    f.close()

def read_file(filename, chunk_size=5242880):
    """
    This function reads the audio to a fom the old file.
    Parameters: filename - a string representing the number of the file, chunk_size - an integer representing the chunks in our file
    Return: None, but data is yielded
    """
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

def transcribe(audio):
    """
    This function transcribes the raw audio file.
    Parameters: audio - raw audio data from the user on JavaScript
    Return: None, but data is yielded
    """

    # writes the raw audio file
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