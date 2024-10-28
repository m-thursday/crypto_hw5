from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from base64 import b64encode
from base64 import b64decode
import socket
import rsa
import sys


#generates cipher and decrypts message using given public key
def verify(plaintext, key, signature):
	#Set key for cipher generation
	Key = RSA.import_key(key)
	#Generate the RSA cipher for encryption
	mHash = SHA256.new(plaintext)
	#encrypt plaintext
	try:
		pkcs1_15.new(Key).verify(mHash, signature)
		print(plaintext.decode('utf-8'))
		print('message verified')
	except(ValueError,TypeError):
		print('compromised connection')	
		


if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = 30375
	#connect the socket to the local machine on the designated port
	s.connect(('127.0.0.1', port))
	
	#parse the received data
	publicKey = s.recv(2048)
	signature = s.recv(256)
	mData = s.recv(1024).decode()
	
	plaintext = mData.encode('utf-8')
	
	verify(plaintext, publicKey, signature)
	
	
	

	
	
