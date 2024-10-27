pfrom base64 import b64encode
from base64 import b64decode
import hashlib
import secrets
import socket
import hmac
import json
import sys

def hmacKey(size):
	return secrets.token_bytes(size)
	

def HMAC(plaintext,key):
	return hmac.new(key, plaintext, hashlib.sha256).digest()
	

if name == '__main__':
	script, uInput = argv
	plaintext = uInput.encode('utf-8')
	
	size = 16
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = 30366
	s.bind('', port)
	s.listen(5)
	
	hmac_key = hmacKey(size)
	
	s = HMAC(plaintext, hmac_key)
	
	data = s, uInput, hmac_key
	
	while True:
		c, addr = s.accept()
		c.send(data)
