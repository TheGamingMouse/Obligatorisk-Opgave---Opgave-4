from socket import *
IPv4 = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((IPv4, serverPort))

while True:
 modifiedSentence = clientSocket.recv(1024)
 print('From server: ', modifiedSentence.decode())
 sentence = input('Message from Client: ')
 clientSocket.send(sentence.encode())
 modifiedSentence = clientSocket.recv(1024)
 print('From Server: ', modifiedSentence.decode())