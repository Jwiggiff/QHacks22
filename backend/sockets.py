import asyncio
import websockets
import json
import secrets
from transcribe_text import transcribe

JOIN = {}
async def start(websocket):
    """
    Handles a connection from the initial audio file.
 
    """
    connected = {websocket}
    join_key = secrets.token_urlsafe(12)
    JOIN[join_key] = connected
    try:
        # Send the secret access tokens to the browser of the first player,
        # where they'll be used for building "join" and "watch" links.
        event = {
                "type": "init",
                "join": join_key,}
        await websocket.send(json.dumps(event))
    finally:
        del JOIN[join_key]


async def join(websocket, join_key):
    """
    Handles a connection from a second audio file
    """
    try:
        connected = JOIN[join_key]
    except KeyError:
        return
    # Register to receive moves from this game.
    try:
        connected.add(websocket)
    except:
        connected.remove(websocket)

async def handler(websocket, path):
    while True:
        message = await websocket.recv()
        event = json.loads(message)
        assert event["type"] == 'init'
        # print(message)
        if message['type'] == 'recording':
            print("recording received")
            text = transcribe(message['audio'])
            await websocket.send(json.dumps({"type": "transcription", "message": text}))
        elif message['type'] == 'join':
            await join(websocket, message['id'])
        else:
            await start(websocket)

async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future() # run forever


if __name__ == "__main__":
    asyncio.run(main()) 
