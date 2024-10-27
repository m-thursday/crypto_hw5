from base64 import b64encode
from base64 import b64decode
import hashlib
import socket
import hmac
import json
import sys

def HMAC(key, plaintext):
	return hmac.new(key, plaintext, hashlib.sha256).digest()
	
def verify(m, message):

	if(m == message):
		print('message verified')
	else:
		print('compromised connection')	

if name == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	port = 30366
	s.connect(('127.0.0.1', port))
	
	sig, message, key = s.recv(1024).decode()
	
	m = HMAC(key, message)
	
	verify(m,message)
	
	

		
			
