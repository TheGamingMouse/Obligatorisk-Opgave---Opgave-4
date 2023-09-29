from socket import *
import threading
import random
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


def HandleClient(connectionSocket, address):
 connectionSocket.send('Type "Random", "Add", or "Subtract" to get the corresponding function.'.encode())
 sentence = connectionSocket.recv(1024).decode()
 txtRecieved = 'From client {addr}: ', sentence
 txtString = str(txtRecieved)
 txtStart = txtString.format(addr = addr)
 print(txtStart)
 connectionSocket.send(' '.encode())

 if 'Random' in sentence:
  handleRandom(connectionSocket, addr)
 
 elif 'Add' in sentence:
  handleAdd(connectionSocket, addr)

 elif 'Subtract' in sentence:
  handleSubtract(connectionSocket, addr)
 
 else:
  handleWrongCommand(connectionSocket, addr)


def handleWrongCommand(connectionSocket, address):
 connectionSocket.send('Wrong command, remember to capitalize the first letter. Connection ended'.encode())
 print('Wrong command from client: ', addr)
 print('Connection closed for client: ', addr)
 connectionSocket.close()


def handleRandom(connectionSocket, address):
 connectionSocket.send('Type two numbers, the server will respond with a random number between them.'.encode())
 sentence = connectionSocket.recv(1024).decode()
 txtRecieved = 'From client {addr}: ', sentence
 txtString = str(txtRecieved)
 txtStart = txtString.format(addr = addr)
 print(txtStart)
 x = sentence.split(' ')
 numStr1 = x[0]
 numStr2 = x[1]
 num1 = int(numStr1)
 num2 = int(numStr2)
 num = random.randrange(num1,num2)
 numStr = str(num)
 connectionSocket.send(numStr.encode())
 connectionSocket.send('Connection ended'.encode())
 print('Connection closed for client: ', addr)
 connectionSocket.close()


def handleAdd(connectionSocket, address):
 connectionSocket.send('Type two numbers, the server will then add them together.'.encode())
 sentence = connectionSocket.recv(1024).decode()
 txtRecieved = 'From client {addr}: ', sentence
 txtString = str(txtRecieved)
 txtStart = txtString.format(addr = addr)
 print(txtStart)
 x = sentence.split(' ')
 a = x[0]
 b = x[1]
 a2 = int(a)
 b2 = int(b)
 y = a2 + b2
 z = str(y)
 txt = 'The addition of {first} and {second} equals: ', z
 txtCalc = str(txt)
 calculation = txtCalc.format(first = a, second = b)
 print(calculation)
 connectionSocket.send(calculation.encode())
 connectionSocket.send('Connection ended'.encode())
 print('Connection closed for client: ', addr)
 connectionSocket.close()


def handleSubtract(connectionSocket, address):
 connectionSocket.send('Type two numbers, the server will then subtract them from each other.'.encode())
 sentence = connectionSocket.recv(1024).decode()
 txtRecieved = 'From client {addr}: ', sentence
 txtString = str(txtRecieved)
 txtStart = txtString.format(addr = addr)
 print(txtStart)
 x = sentence.split(' ')
 a = x[0]
 b = x[1]
 a2 = int(a)
 b2 = int(b)
 y = a2 - b2
 z = str(y)
 txt = 'The subtraction of {first} and {second} equals: ', z
 txtCalc = str(txt)
 calculation = txtCalc.format(first = a, second = b)
 print(calculation)
 connectionSocket.send(calculation.encode())
 connectionSocket.send('Connection ended'.encode())
 print('Connection closed for client: ', addr)
 connectionSocket.close()


print('The server is ready to receive')
while True:
 connectionSocket, addr = serverSocket.accept()
 print('Connection from client, address:',addr)
 threading.Thread(target=HandleClient,args=(connectionSocket,addr)).start()