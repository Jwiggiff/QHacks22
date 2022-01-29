import asyncio
import websockets
import json
from transcribe_text import send_receive

async def handler(websocket):
    while True:
        message = await websocket.recv()
        message = json.loads(message)
        print(message)
        if message['type'] == 'recording':
            send_result, receive_result = await send_receive(message['audio'])

async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future() # run forever


if __name__ == "__main__":
    asyncio.run(main())
