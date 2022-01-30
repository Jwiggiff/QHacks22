import asyncio
import websockets
import json
import secrets
from transcribe_text import transcribe

JOIN = {}

async def start(websocket, join_key):
    """
    Handles a connection from the initial audio file.
 
    """
    connected = {websocket}
    # join_key = secrets.token_urlsafe(12)
    JOIN[join_key] = connected
    try:
        # Send the secret access tokens to the browser of the first player,
        # where they'll be used for building "join" and "watch" links.
        event = {
                "type": "init",
                "join": join_key,}
        await websocket.send(json.dumps(event))
    except:
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
        try: 
            message = await websocket.recv()
            event = json.loads(message)
            # print(message)
            if event['type'] == 'recording':
                print("recording received")
                text = transcribe(event['audio'])
                connected = JOIN[event['id']]
                for connection in connected:
                    await connection.send(json.dumps({"type": "transcription", "message": text, "time": event['time']}))
            elif event['type'] == 'join':
                await join(websocket, event['id'])
            else:
                await start(websocket, event['id'])
        except:
            print("Connection closed")
            break

async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future() # run forever


if __name__ == "__main__":
    asyncio.run(main()) 
