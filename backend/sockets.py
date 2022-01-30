import asyncio
from os import environ
import os
import signal
import websockets
import json
import secrets
from transcribe_text import transcribe
from translate import translate

# global variable defining the join dictionary
JOIN = {}

async def start(websocket, join_key):
    """
    This function handles a connection from the initial audio file.
    Parameters: websocket - an object representing the websocket, join_key - a string representing the room ID
    Return: None
    """
    # this stores the websocket inside a new dictionary
    connected = [{"socket": websocket, "lang": "en"}]
    JOIN[join_key] = connected
    
    # stores join key in a dictionary called event, deletes when exception is raised.
    try:
        event = {
                "type": "init",
                "join": join_key,}
        await websocket.send(json.dumps(event))
    except:
        del JOIN[join_key]


async def join(websocket, join_key, lang):
    """
    This function handles a connection from consecutive audio files
    Parameters: websocket - an object representing the websocket, join_key - a string representing the room ID
    Return: None
    """
    # stores the join key in the global dictionary except if the key doesn't exist
    try:
        connected = JOIN[join_key]
    except KeyError:
        return
    # adds websocket to the global dictionary, removes if false
    try:
        connected.append({"socket": websocket, "lang": lang})
    except:
        connected.remove(websocket)


async def handler(websocket):
    """
    This function handles a connection from consecutive audio files
    Parameters: websocket - an object representing the websocket
    Return: None
    """
    # ensures that the handler always sends and receives until while loop ends
    while True:
        # starts, transcribes, and joins the websocket unless the connection is closed
        try: 
            message = await websocket.recv()
            event = json.loads(message)
            if event['type'] == 'recording':
                print("recording received")
                connected = JOIN[event['id']]
                for connection in connected:
                    await connection['socket'].send(json.dumps({"type": "loading"}))
                text = transcribe(event['audio'])
                print(text)
                for connection in connected:
                    print(connection)
                    translated_text = translate(text, connection['lang'])
                    print(translated_text)
                    await connection['socket'].send(json.dumps({"type": "transcription", "message": translated_text, "time": event['time']}))
            elif event['type'] == 'join':
                print(message)
                await join(websocket, event['id'], event['lang'])
            else:
                print(message)
                await start(websocket, event['id'])
        except websockets.exceptions.ConnectionClosedOK:
            print("Connection closed")
            break

async def main():
    """
    This function controls the flow of execution.
    Parameters: None
    Return: None
    """
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    signal.signal(signal.SIGTERM, stop.set_result)
    # loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    async with websockets.serve(handler, "", int(os.environ.get("PORT", "8001"))):
        await stop

if __name__ == "__main__":
    asyncio.run(main()) 
