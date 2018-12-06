import asyncio
import aiohttp
from aiohttp import ClientSession


async def main():
    session = ClientSession()

    async with session.ws_connect('http://0.0.0.0:8080/ws') as ws:

        await ws.send_str('Hello server! It is WS Client!')

        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                print(msg.data)
                break

            elif msg.type == aiohttp.WSMsgType.ERROR:
                break


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(main())]
    wait_tasks = asyncio.wait(tasks)
    loop.run_until_complete(wait_tasks)
    loop.close()

