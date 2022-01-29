import base64
import websockets
import asyncio
import json
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# the AssemblyAI endpoint we're going to hit
URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"

# sends and receives webhook to display sound in terminal
async def send_receive(audio):
   print(f'Connecting websocket to url ${URL}')
   async with websockets.connect(
       URL,
       extra_headers=(("Authorization", os.getenv('AUTH_KEY'))),
       ping_interval=5,
       ping_timeout=20
   ) as _ws:
       run = await asyncio.sleep(0.1)
       print("Receiving SessionBegins ...")
       session_begins = await _ws.recv()
       print(session_begins)
       print("Sending messages ...")
       async def send(audio):
               try:
                #    data = base64.b64encode(audio).decode("utf-8")
                   json_data = json.dumps({"audio_data": str(audio)})
                   run = await _ws.send(json_data)
               except websockets.exceptions.ConnectionClosedError as e:
                   print(e)
                   assert e.code == 4008
               except Exception as e:
                   assert False, "Not a websocket 4008 error"
               run = await asyncio.sleep(0.01)

       async def receive():
           while st.session_state['run']:
               try:
                   result_str = await _ws.recv()
                   # ensures only full sentences are displayed
                   if json.loads(result_str)['message_type'] == 'FinalTranscript': 
                        print(json.loads(result_str)['text'])
                        return json.loads(result_str)['text']
               except websockets.exceptions.ConnectionClosedError as e:
                   print(e)
                   assert e.code == 4008
                   break
               except Exception as e:
                   assert False, "Not a websocket 4008 error"
    #    send_result, receive_result = await asyncio.gather(send(), receive())
    #    return send_result, receive_result
       return await asyncio.gather(send(audio), receive())

# calls the send_recieve function
# asyncio.get_event_loop().run_until_complete(send_receive())
# currently; websockets allow continuous connection between myself and the server
# what we want: websocket that connects between the front and the back-end; ensure that you can pick up audio (from English to other languages)
# https://websockets.readthedocs.io/en/stable/
# we only want a server
