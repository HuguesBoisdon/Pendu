

playing = True 
newGame = True

maxTries = 8
tryCount = maxTries

word = ""
wordTest = ""
wordDisp = ""

while playing :

    if(wordDisp == word):
        print("Gagné !")
        playing = False

    elif(tryCount > 0):

        if(newGame):

            word = rndWord()
            wordTest = word
            wordDisp = word[0] + "_"*(len(word) - 1)
            newGame = False
        
        print(wordDisp)
        letter = input("Entrez une lettre :").upper()

        matchCount = 0
        while(letter in wordTest):

            lInd = wordTest.index(letter)
            wordDisp[lInd] = word[lInd]
            wordTest[lInd] = " "
            matchCount += 1

        if(matchCount == 0) :
            
            tryCount -=1
            print("nop")
    else:
        print("Perdu !")
        playing = False
        
