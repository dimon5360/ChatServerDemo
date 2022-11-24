
import asyncio
from websockets import connect

class TestWSClient():
    
    def __init__(self, host, port):

        self.__host = host
        self.__port = port

    def run(self):
        
        uri = "ws://{}:{}".format(self.__host, self.__port)
        print("websocket client, try to connect to", uri)

        asyncio.run(self.__hello(uri))

    async def __hello(self, uri):

        async with connect(uri) as websocket:
            await websocket.send("Hello world!")
            resp = await websocket.recv()
            print("Got from server:", resp)
