from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from base64 import b64encode
from base64 import b64decode
from sys import argv
import socket

def rsaKey(size): 
	#generate key data for Alice given a key size
	key = RSA.generate(size)
	priv_key = key.export_key()
	pub_key = key.publickey().export_key()
	return priv_key, pub_key #Alice key pair

def signRSA(plaintext, key):
	#Set key for cipher generation
	Key = RSA.import_key(key)
	#Generate the RSA cipher for encryption
	mHash = SHA256.new(plaintext)
	#encrypt plaintext
	ciphertext = pkcs1_15.new(Key).sign(mHash)
	return ciphertext
	
def sendData(c,sig,pbKey,uInput):
	#Cleaner method for sending all the data
	c.sendall(pbKey)
	c.sendall(sig)
	c.sendall(uInput.encode())
	

if __name__ == '__main__':
	#take in the script name and the message from command line
	script, uInput = argv
	#ensure correct message length
	while len(uInput) != 18:
		uInput = input("Give an 18 byte message for RSA: ")
	#encode plaintext for encryption
	plaintext = uInput.encode('utf-8')
	#create a socket for communication
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#designate a port on the local machine
	host = '127.0.0.1'
	port = 30375
	#bind the socket to the designated port with an empty parameter for the local ip
	s.bind((host, port))
	#socket in listening mode
	s.listen(5)
	#key size
	size = 2048
	#collect key data to use
	prKey, pbKey = rsaKey(size)
	#collect RSA signature
	sig = signRSA(plaintext, prKey)
	
	while True:
		#estabolish connection
		c, addr = s.accept()
		#send Alice public key to Bob for verifying
		#along with the rest of the data
		sendData(c,sig,pbKey,uInput)
		#close out the connection
		c.close()
		#break the while loop
		break
	
