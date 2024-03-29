import serial, time

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

def clearScreen():
    for i in range(50):
        print""


while True:
    clearScreen()
    #text generator http://www.network-science.de/ascii/
    print """

            ___           ___                       ___           ___     
           /\__\         /\  \          ___        /\__\         /\__\    
          /:/  /        /::\  \        /\  \      /:/  /        /:/  /    
         /:/__/        /:/\:\  \       \:\  \    /:/__/        /:/  /     
        /::\  \ ___   /::\~\:\  \      /::\__\  /::\__\____   /:/  /  ___ 
       /:/\:\  /\__\ /:/\:\ \:\__\  __/:/\/__/ /:/\:::::\__\ /:/__/  /\__\\
       \/__\:\/:/  / \/__\:\/:/  / /\/:/  /    \/_|:|~~|~    \:\  \ /:/  /
            \::/  /       \::/  /  \::/__/        |:|  |      \:\  /:/  / 
            /:/  /        /:/  /    \:\__\        |:|  |       \:\/:/  /  
           /:/  /        /:/  /      \/__/        |:|  |        \::/  /   
           \/__/         \/__/                     \|__|         \/__/    
    """
    print """
             _____ _____ _____ _____ _____ _____ _____ _____ _____ 
            |   __|   __|   | |  _  | __  |  _  |_   _|     | __  |
            |  |  |   __| | | |     |    -|     | | | |  |  |    -|
            |_____|_____|_|___|__|__|__|__|__|__| |_| |_____|__|__|



    """

    while True:
        print "type you user name"
        name = raw_input(">")
        if 10 > len(name) > 0:
            break
        print "sorry try a diffrent user"
    print "retriving %s's data" %name
    print "..."
    ser = serial.Serial(7,19200)
    time.sleep(1)
    print "..."
    time.sleep(2)
    print "..."
    time.sleep(3)
    print "..."
    time.sleep(1)
    print "retrived data"
    time.sleep(2)
    print "printing"
    time.sleep(3)

    ser.write(chr(0x1B)+"@") #reset printer
    ser.write(chr(0x1B)+"a1") #center the text

    #ser.write(chr(0x1B)+chr(0x21)+chr(0x01))
    #ser.write(chr(0x1B)+chr(0x40)+"1") #bold NOT

    #ser.write(chr(0x1B)+chr(0x20)+"0") # set bold?

    #ser.write(chr(0x1B)+chr(0x0E)) #set double width
    #ser.write(chr(0x1B)+chr(0x14)) #disable double width
    ser.write("---------------------------")
    ser.write(chr(0x0A))  

    ser.write(chr(0x1B)+chr(0x21)+chr(0x30))
    ser.write("%s's"%name)
    ser.write(chr(0x0A))
    ser.write("HAIKU")  
    ser.write(chr(0x0A))          
  
    ser.write(chr(0x1B)+"@") #reset printer
    ser.write(chr(0x1B)+"a1") #center the text

    ser.write("---------------------------")
    ser.write(chr(0x0A))

    print "print line 1"
    ser.write(" "+getWordsByKeys(getRandomSum(5)))
    ser.write(chr(0x0A))
    print "done"
    time.sleep(1)

    print "print line 2"    
    ser.write(" "+getWordsByKeys(getRandomSum(7)))
    ser.write(chr(0x0A))
    print "done"
    time.sleep(1)

    print "print line 3"    
    ser.write(" "+getWordsByKeys(getRandomSum(5)))
    ser.write(chr(0x0A)+chr(0x0A))
    print "done"

    for i in range(4):    
        ser.write(chr(0x0A)) 

    time.sleep(1)
    print "disconnecting from printer"
    time.sleep(2)    
    print "..."
    time.sleep(1)
    print "..."
    time.sleep(3) 
    ser.close()
    print "disconnected"    
    clearScreen()   