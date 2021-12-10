# -*- coding: utf-8 -*-
"""

Created on Fri Dec 10 08:20:17 2021
@author: Augustin Bouveau / Hugues Boisdon
TODO : ALL

"""

from os import close
from random import randint

def wordChoice():
    fileName = "mots.txt"
    file = open(fileName,'r')
    content = file.readlines()
    word = content[randint(0, len(content))]
    file.close()
    return word.upper().strip()
    

def display(wordDisp):

    print("\n")
    print(wordDisp)
    letter = input("Entrez une lettre :").upper()

    return letter

def replaceLetter(letter, word, wordTest, wordDisp):
    matchCount = 0
    while(letter in wordTest):
        lInd = wordTest.index(letter)
        wordDisp = wordDisp[:lInd] + word[lInd] + wordDisp[lInd +1:]
        wordTest = wordTest[:lInd] + " " + wordTest[lInd +1:]
        matchCount += 1
    return wordTest, wordDisp, matchCount

def getHighscore(path):
    text = open(path,"r")
    valRen = text.readlines()[0].strip()
    text.close()
    return valRen

def setHighscore(path, score):
    if(score > int(getHighscore(path))):
        print("BG !!!! Nouveau highscore !")
        text = open(path,"w")
        text.write(str(score))
        text.close()