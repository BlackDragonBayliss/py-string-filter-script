
# Create the main function
def main():
    # declare any necessary variable(s)
    boolUserStillAddingWords = True
    boolAskingUserInput = True
    listWords = []

    # // Loop: while the user want to enter more words (minimum of 8)
    # // Prompt for, input and store a word (string) into a list
    while (boolUserStillAddingWords):
        # if(lengthOfListWords < 8):

        # Ask "add more words until 8 minimum words in list.
        print("Current count of words is", len(listWords),'-', "please enter more until a minimum of 8 words")
        inputString = input("Please add a word: ")
        listWords.append(inputString)
        if (len(listWords) >= 8):
            while(boolAskingUserInput):
                inputAddMoreWords = input("Add more words? (y/n)")
                if (inputAddMoreWords == "y" or inputAddMoreWords == 'n'):
                    if(inputAddMoreWords == "y"):
                        break
                    if(inputAddMoreWords == "n"):
                        boolAskingUserInput = False
                        boolUserStillAddingWords = False
                        #     // Pass the list of words to following functions, and perform the manipulations
                        #
                        #     //  to produce and return a new, modified, copy of the list.
                        #     //  NOTE: None of the following functions can change the list parameter it
                        #     //  receives – the manipulated items must be returned as a new list.
                        listSortByIncreasingLength = SortByIncreasingLength(listWords)
                        listSortByDecreasingLength = SortByDecreasingLength(listWords)
                        listSortByTheMostVowels = SortByTheMostVowels(listWords)
                        listSortByTheLeastVowels = SortByTheLeastVowels(listWords)
                        listCapitalizeEveryOtherCharacter =CapitalizeEveryOtherCharacter(listWords)
                        listReverseWordOrdering = ReverseWordOrdering(listWords)
                        listFoldWordsOnMiddleOfList = FoldWordsOnMiddleOfList(listWords)

                        # Display the contents of the modified lists of words
                        # Ask if the user wants to process another list of words

                        DisplayModifiedListsOfWords(listSortByIncreasingLength,listSortByDecreasingLength,
                                                    listSortByTheMostVowels,listSortByTheLeastVowels,
                                                    listCapitalizeEveryOtherCharacter,listReverseWordOrdering,
                                                    listFoldWordsOnMiddleOfList)

                        boolCreateAnotherList = AskUserProcessAnotherList()
                        if(boolCreateAnotherList):
                            main()
                        break
                else:
                    #prompt user "Please enter correct syntax"
                    print("Please enter \"y\" or \"n\"")
                    continue
        continue

# Pass the list of words to following functions, and perform the manipulations

# to produce and return a new, modified, copy of the list.
# NOTE: None of the following functions can change the list parameter it
# receives – the manipulated items must be returned as a new list.

def SortByIncreasingLength(listWords):
    calculatedList = sorted(listWords, key=lambda word: len(word))
    print(calculatedList)
    return calculatedList
def SortByDecreasingLength(listWords):
    calculatedList = sorted(listWords, key=lambda word: len(word), reverse=True)
    print(calculatedList)
    return calculatedList
def SortByTheMostVowels(listWords):
    print('SortByMostVowels')
    calculatedList = sorted(listWords, key=lambda word :AlgoSortVowels(word), reverse=True)
    print(calculatedList)
    return calculatedList
def SortByTheLeastVowels(listWords):
    print('SortByLeastVowels')
    calculatedList = sorted(listWords, key=lambda word: AlgoSortVowels(word))
    print(calculatedList)
    return calculatedList
def CapitalizeEveryOtherCharacter(listWords):
    print('CapitalizeEveryOtherCharacter')
    calculatedList = []
    for word in listWords:
        calculatedWord = AlgoCapitalizeEveryOtherCharacter(word)
        calculatedList.append(calculatedWord)
    print(calculatedList)
    return calculatedList
def ReverseWordOrdering(listWords):
    calculatedList = AlgoReverseList(listWords)
    print(calculatedList)
    return calculatedList

#No idea what the professor means to sort by ??
def FoldWordsOnMiddleOfList(listWords):
    calculatedList = sorted(listWords, key=lambda word: len(word))
    print(calculatedList)
    return calculatedList

def AlgoSortVowels(str):
    # Intializing count variable to 0
    count = 0
    # Creating a set of vowels
    vowel = set("aeiouAEIOU")
    # Loop to traverse the alphabet in the given string
    for alphabet in str:
        # If alphabet is present in set vowel
        if alphabet in vowel:
            count = count + 1
    return count

def AlgoCapitalizeEveryOtherCharacter(str):
    currentIndex = 0
    calculatedWord = ""
    splitList = list(str)

    for character in splitList:
        if(currentIndex == 0):
            calculatedWord += character
            currentIndex += 1
            continue
        if (currentIndex % 2 != 0):
            currentCharacter = character.capitalize()
            calculatedWord += currentCharacter
        if(currentIndex % 2 == 0):
            currentCharacter = character
            calculatedWord += currentCharacter
        currentIndex += 1
    return calculatedWord

def AlgoReverseList(listWords):
    calculatedList = []
    boolCalculating = True
    currentIndex = 0
    lengthListWords = len(listWords)
   # Calculate list in descending order
    while (boolCalculating):
        # Calculate current list index starting from the last indexed value
        calculatedListIndex = lengthListWords-(currentIndex+1)
        calculatedList.append(listWords[calculatedListIndex])
        currentIndex += 1
        if(calculatedListIndex == 0):
            boolCalculating = False
    return calculatedList


# Display the contents of the modified lists of words
# Ask if the user wants to process another list of words

def DisplayModifiedListsOfWords(listSortByIncreasingLength,listSortByDecreasingLength,
                                                    listSortByTheMostVowels,listSortByTheLeastVowels,
                                                    listCapitalizeEveryOtherCharacter,listReverseWordOrdering,
                                                    listFoldWordsOnMiddleOfList):
    # Display the contents of the modified lists of words
    print("Below is the sorted lists:")
    print("Sorted by increasing length:",listSortByIncreasingLength)
    print("Sorted by decreasing length:", listSortByDecreasingLength)
    print("Sorted by the most vowels:", listSortByTheMostVowels)
    print("Sorted by least vowels:", listSortByTheLeastVowels)
    print("List of words: capitalize every other character:", listCapitalizeEveryOtherCharacter)
    print("List of words: reverse order:", listReverseWordOrdering)
    print("List of words: fold words on middle of list:", listFoldWordsOnMiddleOfList)

def AskUserProcessAnotherList():
    boolAskingUserInput = True
    boolCreateAnotherList = None
    inputAddAnotherList = input("Process another list? (y/n) ")

    while(boolAskingUserInput):
        if (inputAddAnotherList == "y" or inputAddAnotherList == 'n'):
            if (inputAddAnotherList == "y"):
                boolAskingUserInput = False
                boolCreateAnotherList = True
                break
            if (inputAddAnotherList == "n"):
                boolAskingUserInput = False
                break
        else:
            # prompt user "Please enter correct syntax"
            print("Please enter \"y\" or \"n\"")
            continue
    return boolCreateAnotherList
main()