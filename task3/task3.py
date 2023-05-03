from modules.deck import Deck
from time import sleep
from modules.gronkyutil import convertCardToId
from modules.gronkyutil import TITLE, GANG

def main():
    print("Welcome to Gronky Cards\n")
    print("Shuffling Cards", end="")
    thinking()

    deck = Deck()
    playerHand = []

    cardCount = int(input("How many cards would you like?: "))

    for i in range(cardCount):
        playerHand.append(deck.draw()) # Single line

    done = False
    while not done:
        print()
        print("Menu")
        print("\t(1) Display hand")
        print("\t(2) Sort by title")
        print("\t(3) Sort by gang")
        print("\t(4) Search for card")
        print("\t(5) Quit")
        choice = int(input("Choose an option: "))
        print()

        if choice == 1:
            displayHand(playerHand)
        elif choice == 2:
            sortByTitle(playerHand) # Single line
        elif choice == 3:
            sortByGang(playerHand) # Single line
        elif choice == 4:
            searchForCard(playerHand) # Single line
        elif choice == 5:
             done = True

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.15)
    print()

def displayHand(hand):
    for card in hand:
        print(card) # Not a single line. The entire function body

# Add other functions you need below
def sortByTitle(hand):
    print("Sorting by selection", end="")
    thinking()
    for i in range(len(hand)):
        minIndex = i
        for j in range(i+1, len(hand)):
            if TITLE.index(hand[j].getTitle()) < TITLE.index(hand[minIndex].getTitle()):
                minIndex = j
        hand[i], hand[minIndex] = hand[minIndex], hand[i]

def sortByGang(hand):
    print("Sorting by insertion", end="")
    thinking()
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(hand)):
            if GANG.index(hand[i].getGang()) < GANG.index(hand[i-1].getGang()):
                hand[i-1], hand[i] = hand[i], hand[i-1]
                sorted = False

def binaryCardSearch(hand, left, right, x):
    hand.sort()
    mid = left + (right - left) // 2
    if left > right:
        return "This card is not in your hand"

    if hand[mid] == x:
        return "This card is in your hand"
    
    elif hand[mid] > x:    #x is smaller than the mid
        return binaryCardSearch(hand, left, mid-1, x)
    
    elif hand[mid] < x:    #x is larger than mid
        return binaryCardSearch(hand, mid+1, right, x)
    
    else:
        return "This card is not in your hand"
            

def searchForCard(hand):
    valid = False
    while not valid:
        num = 1
        for i in TITLE:
            print(str(num) + "):  " + str(i))
            num += 1
        title = input("What title are you searching for:\n\t")
        try:
            int(title)
        except:
            print("that is not a valid response\n")
        else:
            valid = True
            title = TITLE[int(title)-1]
    valid = False
    while not valid:
        num = 1
        for i in GANG:
            print(str(num) + "):  " + str(i))
            num += 1
        gang = input("What gang are you searching for:\n\t")
        try:
            int(gang)
        except:
            print("that is not a valid response\n")
        else:
            gang = GANG[int(gang)-1]
            valid = True

    xId = convertCardToId(title, gang)
    handIds = [i.getID() for i in hand]
    print("Searching", end="")
    thinking()
    print(binaryCardSearch(handIds, 0, len(handIds)-1, xId))


main()