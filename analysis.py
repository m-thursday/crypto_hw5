from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from sys import argv
import hashlib
import secrets
import hmac
import time

def hmacKey(size):
	#HMAC key generation (random 16 byte long token)
	return secrets.token_bytes(size)
	

def HMAC(plaintext,key):
	#Use the generated key to create a digest
	return hmac.new(key, plaintext, hashlib.sha256).digest()
	
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
	
def verify(plaintext, key, sig1, p):
	#Set key for cipher generation
	Key = RSA.import_key(key)
	#Generate the RSA cipher for encryption
	mHash = SHA256.new(plaintext)
	#encrypt plaintext
	try:
		pkcs1_15.new(Key).verify(mHash, sig1)
		if p == 0:
			print('message verified')
	except(ValueError,TypeError):
		print('compromised connection')		
	
if __name__ == '__main__':
	
	script, uInput = argv
	
	plaintext = uInput.encode('utf-8')
	
	while len(uInput) != 7:
		uInput = input("Give a 7 byte message for analysis: ")
		
	tmpHMAC = 0
	tmpSign = 0
	tmpVer = 0
	p = 0
		
	size = 16
	hmac_key = hmacKey(size)	
	for i in range (99):
		start = time.time()
		sig = HMAC(plaintext, hmac_key)
		end = time.time()
		tmpHMAC += (end - start)
	
	size = 2048
	prKey, pbKey = rsaKey(size)
	for i in range (99):
		start = time.time()
		s = signRSA(plaintext, prKey) 
		end = time.time()
		tmpSign += (end - start)
		start1 = time.time()
		verify(plaintext, pbKey, s, p)
		end1 = time.time()
		tmpVer += (end1 - start1)
		p += 1
	
	averageHMAC = tmpHMAC / 100
	averageSign = tmpSign / 100
	averageVerify = tmpVer / 100
	
	print("--------------------------------------------------")	
	print("Average HMAC Generation")
	print("--------------------------------------------------")
	print(averageHMAC)
	print("--------------------------------------------------")
	print("Average RSA Signing")
	print("--------------------------------------------------")
	print(averageSign)
	print("--------------------------------------------------")
	print("Average RSA Verification")
	print("--------------------------------------------------")
	print(averageVerify)
