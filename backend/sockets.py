import asyncio
import websockets
from transcribe_text import send_recieve
async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)
        if message.type == 'recording':
            send_result, receive_result = await send_recieve()

async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future() # run forever


if __name__ == "__main__":
    asyncio.run(main())
