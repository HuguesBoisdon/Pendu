import funk

playing = True 
newGame = True

maxTries = 8
tryCount = maxTries

word = ""
wordTest = ""
wordDisp = " "

while playing :

    if(wordDisp == word):
        print("Gagné !")
        playing = False

    elif(tryCount > 0):

        if(newGame):

            word = funk.wordChoice()
            wordTest = word
            wordDisp = word[0] + "_"*(len(word) - 1)
            newGame = False
        
        print("\n")
        print(word)
        print(wordDisp)
        print(word == wordDisp)
        letter = input("Entrez une lettre :").upper()

        matchCount = 0
        while(letter in wordTest):

            lInd = wordTest.index(letter)
            wordDisp = wordDisp[:lInd] + word[lInd] + wordDisp[lInd +1:]
            wordTest = wordTest[:lInd] + " " + wordTest[lInd +1:]
            matchCount += 1

        if(matchCount == 0) :
            tryCount -=1
            print("nop")
    else:
        print("Perdu !")
        playing = False
        