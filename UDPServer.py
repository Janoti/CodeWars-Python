from socket import *


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print "The server is ready to receive"

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	resposta = message.split('$')

	if (resposta[0] == '1'):
		modifiedMessage = resposta[1].upper()
	else:
		modifiedMessage = resposta[1].lower()

	
	serverSocket.sendto(modifiedMessage, clientAddress)
