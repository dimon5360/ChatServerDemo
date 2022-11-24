
import asyncio
from http import client
from websockets import serve
import random
import json

class WSserver():

    def __init__(self, host, port):
        self.__connections: dict[str, Any] = {}
        self.__id_max = 65536
        self.__host = host
        self.__port = port

    def run(self):

        print("Start listening ws://{0}:{1}".format(self.__host, self.__port))
        asyncio.run(self.__run(self.__host, self.__port))

    async def __run(self, host, port):

        async with serve(self.__handle, host, port):
            await asyncio.Future()

    async def __handle(self, websocket):
        
        client_id = random.randint(0, self.__id_max)  
        print("Somebody connected with id #", client_id)

        self.__connections[client_id] = websocket
        await websocket.send(json.dumps({'ID' : client_id}))

        async for message in websocket:
            print("Got message:", message)
            await websocket.send(message)




