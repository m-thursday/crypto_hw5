from Crypto.Hash import SHA256
import secrets
import random
import time

def messageGen(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(secrets.choice(characters) for _ in range(length))

def runCollision(db):
    m = messageGen(random.randrange(5, 15))
    tmp = SHA256.new(m.encode())
    mHash = tmp.digest()[:8]
    db.append((m, mHash))
    
    for i in range(len(db)):
        for j in range(i + 1, len(db)):  
            if db[i][1] == db[j][1]:
                print("Collision found:")
                print("Message 1:", db[i][0], "Hash:", db[i][1])
                print("Message 2:", db[j][0], "Hash:", db[j][1])
                return True 
                
    return False 

if __name__ == '__main__':
    x = 0
    collision = False
    db = []
    t = time.time()
    random.seed(t)
    
    while not collision:
        print("Check", x)  
        x += 1  
        collision = runCollision(db)
