from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode
from base64 import b64decode
import socket
import rsa
import sys

#generates cipher and decrypts message using given public key
def decryptRSA(publicKey, signature): 
	cipher_rsa = PKCS1_OAEP.new(publicKey)
	m = cipher_rsa.decrypt(ciphertext)
	return m
	
def verify(mData, message):

	if(mData == message):
		print('message verified')
	else:
		print('compromised connection')	


if name == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = 30366
	#connect the socket to the local machine on the designated port
	s.connect(('127.0.0.1', port))
	
	#parse the received data
	publicKey, data = s.recv(4096).decode()
	signature, mData = data
	
	message = decryptRSA(publicKey, signature)
	
	verify(mData,message)
	
	

	
	
