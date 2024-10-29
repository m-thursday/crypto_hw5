from Crypto.Hash import SHA256
import secrets
import random
import time

def messageGen(length):
	characters = string.ascii_letters
	return ''.join(secrets.choice(characters) for i in range (length))


if __name__ == '__main__':
	db = []
	t = time.time()
	random.seed(t)
	while True:
		m = messageGen(random.random())
		tmp = SHA256.new(m)
		mHash = tmp[:8]
		db.append((m,mHash))
		for i in range (len(db)):
			for j in range (len(db)):
				if db[i][1] == db[j][1]:
					break
		
