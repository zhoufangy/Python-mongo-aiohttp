from aiohttp import web
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
demo = client.demo_db
# demo.authenticate("dev", "Aa123456")
addr = demo.address
res = addr.find_one()

async def handle(request):
    name = request.match_info.get('userId', "zuo")
    address = res['addr']
    text = "Hello, " + name + " addr = " + address
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)