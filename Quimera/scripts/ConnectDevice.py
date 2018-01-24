from socket import *

def Communication(command):
	host = "192.168.0.10"
	port = 35000
	buffer_size = 1024
	soc = socket(AF_INET, SOCK_STREAM)
	soc.connect((host,port))
	soc.send(bytes(command, "utf-8"))
	dados = soc.recv(buffer_size)
	soc.close()
	return dados
	
