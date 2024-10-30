from base64 import b64encode
from base64 import b64decode
import hashlib
import socket
import hmac

	
def verify(plaintext, key, sig1):
	#verify the message by checking the original signature against a newly generated one
	sig2 = hmac.new(key, plaintext, hashlib.sha256).digest()

	if(sig1 == sig2):
		print('message verified')
	else:
		print('compromised connection')	

if __name__ == '__main__':
	#socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = '127.0.0.1'
	port = 30368
	#estabolish connection
	s.connect((host, port))
	#receive data
	sig = s.recv(1024)
	m = s.recv(1024).decode()
	k = s.recv(1024)
	#verify data
	verify(m.encode(), k, sig)
	
	

		
			
