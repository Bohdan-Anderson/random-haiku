wordDict = {}

import re
import random

# PARSE WORDLIST
for line in open('wordlist.txt', 'r').readlines():
    numOfSyllables = re.findall(r'\d+', line)[0]
    word = line.strip(numOfSyllables)
    word = word.strip("\n")
    if not (numOfSyllables in wordDict):
        wordDict[numOfSyllables] = []
        wordDict[numOfSyllables].append(word)
    else:
        wordDict[numOfSyllables].append(word)

#GET RANDOM KEY
def getRandomKey():
    return random.choice(wordDict.keys())

#GET RANDOM SUM
def getRandomSum(s):
    keys = []
    total = s
    key = getRandomKey()
    keys.append(int(key))
    while (total > 1):
        total = total - int(key)
        if (total < 1): return keys
        key = random.randint(1, total)
        keys.append(key)
    return keys
fullhaiku = ""
#GET WORDS BASED ON SUMS
def getWordsByKeys(keys):
    haiku = ""
    for key in keys:
        word = random.choice(wordDict[str(key)])
        while word in haiku:
            word = random.choice(wordDict[str(key)])
            
        haiku += word + " "
        
        
    return haiku

print getWordsByKeys(getRandomSum(5))
print getWordsByKeys(getRandomSum(7))
print getWordsByKeys(getRandomSum(5))
