from base64 import b64encode
from base64 import b64decode
from sys import argv
import hashlib
import secrets
import socket
import hmac

def hmacKey(size):
	return secrets.token_bytes(size)
	

def HMAC(plaintext,key):
	return hmac.new(key, plaintext, hashlib.sha256).digest()
	

if __name__ == '__main__':
	script, uInput = argv
	
	while len(uInput) != 18:
		uInput = input("Give an 18 byte message for HMAC: ")
	
	plaintext = uInput.encode('utf-8')
	
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = '127.0.0.1'
	port = 30368
	s.bind((host, port))
	s.listen(5)
	
	size = 16
	hmac_key = hmacKey(size)
	sig = HMAC(plaintext, hmac_key)
		
	while True:
		c, addr = s.accept()
		c.sendall(sig)
		c.sendall(uInput.encode())
		c.sendall(hmac_key)
			
		c.close()
			
		break
