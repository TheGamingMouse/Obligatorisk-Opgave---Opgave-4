from socket import *
import threading
import random
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


def HandleClient(connectionSocket, address):
 connectionSocket.send('Type "Random" or "Calculator" to get the corresponding function.'.encode())
 sentence = connectionSocket.recv(1024).decode().lower()
 txtRecieved = 'From client {addr}: ', sentence
 txtString = str(txtRecieved)
 txtStart = txtString.format(addr = addr)
 print(txtStart)
 connectionSocket.send(' '.encode())

 if 'random' in sentence:
  handleRandom(connectionSocket, addr)
 
 elif 'calculator' in sentence:
  handleCalculator(connectionSocket, addr)

 else:
  handleWrongCommand(connectionSocket, addr)


def handleWrongCommand(connectionSocket, address):
 connectionSocket.send('Wrong command, did you input a valid command word?. Connection ended'.encode())
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


def handleCalculator(connectionSocket, address):
 connectionSocket.send('Type "Add", "Subtract", "Multiply", or "Divide" to get the corresponding function. Type two numbers after the command word, the server will use them for the calculation.'.encode())
 sentence = connectionSocket.recv(1024).decode()
 txtRecieved = 'From client {addr}: ', sentence
 txtString = str(txtRecieved)
 txtStart = txtString.format(addr = addr)
 print(txtStart)

 x = sentence.split(' ')
 a = x[1]
 b = x[2]
 a2 = int(a)
 b2 = int(b)
 
 if 'add' in sentence:
  y = a2 + b2
  z = str(y)
  txt = 'The {calc} of {num1} and {num2} equals: ', z
  txtStr = str(txt)
  txtCalc = txtStr.format(calc = 'addition', num1 = a, num2 = b)
  print(txtCalc)
  connectionSocket.send(txtCalc.encode())
 
 elif 'subtract' in sentence:
  y = a2 - b2
  z = str(y)
  txt = 'The {calc} of {num1} and {num2} equals: ', z
  txtStr = str(txt)
  txtCalc = txtStr.format(calc = 'subtraction', num1 = a, num2 = b)
  print(txtCalc)
  connectionSocket.send(txtCalc.encode())
 
 elif 'multiply' in sentence:
  y = a2 * b2
  z = str(y)
  txt = 'The {calc} of {num1} and {num2} equals: ', z
  txtStr = str(txt)
  txtCalc = txtStr.format(calc = 'multiplication', num1 = a, num2 = b)
  print(txtCalc)
  connectionSocket.send(txtCalc.encode())
 
 elif 'divide' in sentence:
  y = a2 / b2
  z = str(y)
  txt = 'The {calc} of {num1} and {num2} equals: ', z
  txtStr = str(txt)
  txtCalc = txtStr.format(calc = 'divition', num1 = a, num2 = b)
  print(txtCalc)
  connectionSocket.send(txtCalc.encode())
 
 connectionSocket.send('Connection ended'.encode())
 print('Connection closed for client: ', addr)
 connectionSocket.close()
 

print('The server is ready to receive')
while True:
 connectionSocket, addr = serverSocket.accept()
 print('Connection from client, address:',addr)
 threading.Thread(target=HandleClient,args=(connectionSocket,addr)).start()
