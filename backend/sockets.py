import asyncio
import websockets
import json
from transcribe_text import transcribe_a

async def handler(websocket):
    while True:
        message = await websocket.recv()
        message = json.loads(message)
        # print(message)
        if message['type'] == 'recording':
            print("recording received")
            text = transcribe_a(message['audio'])
            print(text)

async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future() # run forever


if __name__ == "__main__":
    asyncio.run(main()) 
