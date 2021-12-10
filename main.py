import funk

playing = True 
newGame = True

maxTries = 8
tryCount = maxTries

word = ""
wordTest = ""
wordDisp = " "
usedLetters = []
validLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]

highscorePath = "highscore.txt"

while playing :

    if(wordDisp == word):
        print(word)
        print("Gagné !")
        playing = False

    elif(tryCount > 0):

        if(newGame):
            print("[[[ HIGHSCORE : "+funk.getHighscore(highscorePath)+" ]]]")
            word = funk.wordChoice()
            wordTest = word
            wordDisp = "_"*len(word)
            newGame = False
            wordTest, wordDisp, matchCount = funk.replaceLetter(word[0], word, wordTest, wordDisp)
        
        print("\n")
        print("-- Il vous reste " + str(tryCount) + " essais ! --")
        letter = funk.display(wordDisp)
        while(not(letter in validLetters) or (letter in usedLetters)):
            if letter in usedLetters:
                print("lettre dejà utilisée")
            if letter not in validLetters:
                print("t con ou qkoi ?")
            letter = funk.display(wordDisp)

        usedLetters.append(letter)

        wordTest, wordDisp, matchCount = funk.replaceLetter(letter, word, wordTest, wordDisp)

        if(matchCount == 0) :
            tryCount -=1
            print("nop")
    else:
        print("Perdu !")
        print(word)
        playing = False

    if(not playing):
        print("\n"*5)
        funk.setHighscore(highscorePath,tryCount)
        resp = ""
        while(resp not in ["O","N"]):
            resp = input("Voulez-vous rejouer ? [O/N] :").upper().strip()
        if resp == "O":
            playing = True
            newGame = True
            tryCount = maxTries
            wordDisp = " "
            usedLetters = []
        