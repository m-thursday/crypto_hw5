from base64 import b64encode
from base64 import b64decode
import hashlib
import socket
import hmac
import json
import sys
	
def verify(plaintext, key, sig1):
	sig2 = hmac.new(key, plaintext, hashlib.sha256).digest()

	if(sig1 == sig2):
		print('message verified')
	else:
		print('compromised connection')	

if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = '127.0.0.1'
	port = 30368
	
	s.connect((host, port))
	
	sig = s.recv(1024)
	m = s.recv(1024).decode()
	k = s.recv(1024)
	
	verify(m.encode(), k, sig)
	
	

		
			
