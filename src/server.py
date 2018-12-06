import aiohttp
from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    print('handle')
    return web.Response(text=text)


async def websocket_handle(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:                        # data = await ws.receive()
        if msg.type == aiohttp.WSMsgType.TEXT:
            await ws.send_str('Hello client! It is ws server')
            if msg.data == 'close':
                break

        elif msg.type == aiohttp.WSMsgType.ERROR:
            break

    await ws.close()
    print('ws close')

    return ws


app = web.Application()
app.add_routes(
    [
        web.get('/ws', websocket_handle),
        web.get('/', handle),
        web.get('/{name}', handle),
    ]
)

web.run_app(app)
