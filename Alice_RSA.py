from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode
from base64 import b64decode
import socket
import rsa
import sys

def rsaKey(size): 
	#generate key data for Alice given a key size
	key = RSA.generate(size)
	priv_key = key.export_key()
	pub_key = key.publickey().export_key()
	return priv_key, pub_key #Alice key pair

def encryptRSA(plaintext, prKey):
	#Generate the RSA cipher for encryption
	cipher_rsa = PKCS1_OAEP.new(prKey)
	#encrypt plaintext
	ciphertext = cipher_rsa.encrypt(plaintext)
	return ciphertext
	

if name == '__main__':
	#take in the script name and the message from command line
	script, uInput = argv
	#encode plaintext for encryption
	plaintext = uInput.encode('utf-8')
	#create a socket for communication
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#designate a port on the local machine
	port = 30366
	#bind the socket to the designated port with an empty parameter for the local ip
	s.bind('', port)
	#socket in listening mode
	s.listen(5)
	#key size
	size = 2048
	#collect key data to use
	prKey, pbKey = rsaKey(size)
	#collect RSA signature
	sig = encryptRSA(plaintext,prKey)
	#create variables to hold signature and message, and public key
	data = sig, uInput
	sendData = pbKey, data
	
	while True:
		#estabolish connection
		c, addr = s.accept()
		#send Alice public key to Bob for verifying
		#along with the rest of the data
		c.send(sendData)
		#close out the connection
		c.close()
		#break the while loop
		break
	
