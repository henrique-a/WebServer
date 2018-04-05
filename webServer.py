# -*- coding: utf-8 -*-

from socket import *
import os

def main():

    fileNameList = os.listdir('html')

    serverPort = 80
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive')

    while True:
        connectionSocket, addr = serverSocket.accept()
        request = connectionSocket.recv(1024)
        response = httpHandler(request, fileNameList)

        connectionSocket.send(response)
        connectionSocket.close()

def httpHandler(request, fileNameList):
    requestWordList = request.split()
    #print(requestWordList)
    if requestWordList[1].decode() is '/':
        file = open('html/index.html')
        response = 'HTTP/1.0 200 OK\r\n\r\n'
        for line in file:
            response = response + line
        return response.encode()

    else:
        fileName = requestWordList[1][1:].decode()
        if fileName in fileNameList:
            file = open('html/' + fileName)
            response = 'HTTP/1.0 200 OK\r\n\r\n'
            for line in file:
                response = response + line

            return response.encode()

        else:
            file = open('html/error.html')
            response = 'HTTP/1.0 200 OK\r\n\r\n'
            for line in file:
                response = response + line

            return response.encode()

if __name__ == '__main__':
    main()
