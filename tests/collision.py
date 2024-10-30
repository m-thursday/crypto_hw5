import hashlib
import secrets

def messageGen(length):
	#set a list of characters for the message generator to use
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #generate the message from the list of characters with a set length
    return ''.join(secrets.choice(characters) for _ in range(length))

def runCollision():
	#initialize variables needed to run the initial collision test
    x = 0 #collision counter
    db = [] #list of all the messages and hashes
    while True:
    	#increment the count
        x += 1
        #generate a message
        m = messageGen(7)
        #generate the hash
        tmp = hashlib.sha256()
        #update the hash with the generated message after encoding
        tmp.update(str.encode(m))
        #take the first 8 bits of the hashed string
        mHash = tmp.digest()[:2]
        #put it in the list as a tuple
        db.append((m, mHash))
        #check for collisions
        for i in range(len(db)):
            for j in range(i + 1, len(db)):
                if db[i][1] == db[j][1]:
                    print(f"Collision Found with {x} Hashes:")
                    print("Message 1:", db[i][0], "Hash:", db[i][1])
                    print("Message 2:", db[j][0], "Hash:", db[j][1])
                    return x
    return -1

def collisionAnalysis(): 
#I made a second function because i like the print statement in the first but this
#runs 20 times and i didnt want to have that many prints so i decided it was a good
#idea to just not have that happen and instead of making the print conditional which
#likely would have been pretty easy since i did it in the analysis file I just decided
#to copy and paste the function and delete the print statement so i will not be
#commenting this function
    x = 0
    db = []
    while True:
        x += 1
        m = messageGen(7)
        tmp = hashlib.sha256()
        tmp.update(str.encode(m))
        mHash = tmp.digest()[:2]
        db.append((m, mHash))
        
        for i in range(len(db)):
            for j in range(i + 1, len(db)):
                if db[i][1] == db[j][1]:
                    return x
    #base case for the function
    return -1

if __name__ == '__main__':
	#run the first function with prints
    y = runCollision()
    
    total_trials = 0
    #calculate the average number of trials needed for collisions
    for i in range(20):
        total_trials += collisionAnalysis()
    
    avg_trials = total_trials / 20
    print("Average Number of Trials for Collision: ", avg_trials)

