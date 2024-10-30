from base64 import b64encode
from base64 import b64decode
from sys import argv
import hashlib
import secrets
import socket
import hmac

def hmacKey(size):
	#for generating the hmac key
	return secrets.token_bytes(size)
	

def HMAC(plaintext,key):
	#returns digest of hmac signature
	return hmac.new(key, plaintext, hashlib.sha256).digest()
	

if __name__ == '__main__':
	#takes user input from the command line
	script, uInput = argv
	#ensures proper message length
	while len(uInput) != 18:
		uInput = input("Give an 18 byte message for HMAC: ")
	#encodes plaintext for usability with signature function
	plaintext = uInput.encode('utf-8')
	
	#set up sockets for file communication
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = '127.0.0.1'
	port = 30368
	s.bind((host, port))
	s.listen(5)
	#Get necessary data from functions
	size = 16
	hmac_key = hmacKey(size)
	sig = HMAC(plaintext, hmac_key)
		
	while True:
		#estabolish connection and send the necessary data
		c, addr = s.accept()
		c.sendall(sig)
		c.sendall(uInput.encode())
		c.sendall(hmac_key)
		#end the connection
		c.close()
			
		break
