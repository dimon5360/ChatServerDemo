
from source.test.testclient import TestWSClient
from source.Core.wsserver import WSserver
from threading import Thread

class AppCore():
    
    def __init__(self, host, port):

        self.__host = host
        self.__port = port
        self.__client = TestWSClient(self.__host, self.__port)
        self.__wsserver = WSserver(self.__host, self.__port)
        
    def run(self):

        serverThread = Thread(target=self.__wsserver.run)
        clientThread = Thread(target=self.__client.run)

        serverThread.start()
        clientThread.start()

        serverThread.join()
        clientThread.join()
