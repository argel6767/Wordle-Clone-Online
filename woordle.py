
import random

def getWord():
    fileDict = {1 : "wordle-La.txt",
                2 : "wordle-Ta.txt"}
    file = fileDict[random.randint(1,2)]
    with open(file, 'r') as fileRead:
        fileContents = fileRead.read()
    listOfWords = fileContents.split("\n")
    
    roundWord = listOfWords[random.randint(0,(len(listOfWords)-1))]
    return roundWord

def makeBoard(word):
    playBoard = [char for char in word]
    emptyList = ['_' for _ in playBoard]
    return emptyList

def wordToDict(word):
    charIndexDict = {}
    
    for index, char in enumerate(word):
        charIndexDict[index] = char
    
    return charIndexDict
    
def contains(guess, actualWord): 
    actualWord = wordToDict(actualWord)
    charsInRightSpot = []
    charsInWord = []
    
    for index , character in enumerate(guess):
        if character in actualWord[index]:
            charsInRightSpot.append(character)
        elif character in actualWord.values():
            charsInWord.append(character)
    
    return charsInRightSpot, charsInWord


def updateBoard(charsInRightSpot, actualWord, previousBoard):
    updatedBoard = []
    for index, chars in enumerate(actualWord):
        if chars in charsInRightSpot:
            updatedBoard.append(chars)
        elif previousBoard[index] != "_":
            updatedBoard.append(previousBoard[index]) 
        else:
            updatedBoard.append("_")
    return updatedBoard

def charNotInTheRightSpot(charsInWord):
    if charsInWord:
        print("The following character(s) are in the word, just not in the right place: ")
        for char in charsInWord:
            print(f"{char}, ", end="")
        print()
        
         
    
    
    

def isGuessCorrect(guess, actual):
    return guess == actual
   


if __name__ == "__main__":
    roundWord = "apple"
    lastBoard = makeBoard(roundWord)
    guesses = []
    flag = True
    
    
    while(flag):
        playerGuess = input("The word is 5 letters. Guess a five letter word! ")
        if (len(playerGuess) != 5):
            print("Not a valid guess, try again!")
            continue
        
        charsInRightSpot, charsInWord = contains(playerGuess, roundWord)
        currentBoard = updateBoard(charsInRightSpot, roundWord, lastBoard)
        print(currentBoard)
        
        charNotInTheRightSpot(charsInWord)
        
        if(isGuessCorrect(playerGuess, roundWord)):
            print("You win!")
            flag = False
            
        lastBoard = currentBoard
        
        

    
            


    


