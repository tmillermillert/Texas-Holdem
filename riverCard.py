import math
import random
from TexasHoldemInclude import printVHand
import sys
def findBestHand(holeCards, communityCards):
    allCards = holeCards + communityCards
    global handToValueDict
    print allCards
    bestHand = None
    for card1 in range(len(allCards)-1):
        if card1 % 2 != 0:
            continue
        for card2 in range(len(allCards)-1):
            if card2 % 2 != 0:
                continue
            for card3 in range(len(allCards)-1):
                if card3 % 2 != 0:
                    continue
                for card4 in range(len(allCards)-1):
                    if card4 % 2 != 0:
                        continue
                    for card5 in range(len(allCards)-1):
                        if card5 % 2 != 0:
                            continue
                        if allCards[card1:card1+2] == allCards[card2:card2+2]:
                            continue
                        if allCards[card1:card1+2] == allCards[card3:card3+2]:
                            continue
                        if allCards[card1:card1+2] == allCards[card4:card4+2]:
                            continue
                        if allCards[card1:card1+2] == allCards[card5:card5+2]:
                            continue
                        if allCards[card2:card2+2] == allCards[card3:card3+2]:
                            continue
                        if allCards[card2:card2+2] == allCards[card4:card4+2]:
                            continue
                        if allCards[card2:card2+2] == allCards[card5:card5+2]:
                            continue
                        if allCards[card3:card3+2] == allCards[card4:card4+2]:
                            continue
                        if allCards[card3:card3+2] == allCards[card5:card5+2]:
                            continue
                        if allCards[card4:card4+2] == allCards[card5:card5+2]:
                            continue
                        moved = True
                        hand = allCards[card1:card1+2] + allCards[card2:card2+2] +\
                        allCards[card3:card3+2] + allCards[card4:card4+2] +\
                        allCards[card5:card5+2]
                        
                        while moved == True:
                            moved = False
                            if int(hand[0:2]) < int(hand[2:4]):
                                temp = hand[2:4] + hand[0:2] + hand[4:]
                                hand = temp
                                moved = True
                            if int(hand[2:4]) < int(hand[4:6]):
                                temp = hand[0:2] + hand[4:6] + hand[2:4]\
                                           + hand[6:]
                                hand = temp
                                moved = True
                            if int(hand[4:6]) < int(hand[6:8]):
                                temp = hand[0:4]+ hand[6:8] + hand[4:6]\
                                           + hand[8:]
                                hand = temp
                                moved = True
                            if int(hand[6:8]) < int(hand[8:]):
                                temp = hand[0:6]+ hand[8:] + hand[6:8]
                                hand = temp
                                moved = True
                        if bestHand == None or handToValueDict[hand] > handToValueDict[bestHand]:
                            bestHand = hand
                            print "hand " + bestHand
                            printVHand(bestHand)
                            print "hand value " + str(handToValueDict[hand])
                        
    print "Community Cards " + communityCards
    print "Hole cards " + holeCards
    print bestHand
    printVHand(bestHand)
    return bestHand 

print "Creating valueToHandsDict"    
f = open("highOrderedHands.txt", "r")
text = f.read(11)
currentValue = 0
valueToHandsDict = {}
while text != "":
    try:
        valueToHandsDict[currentValue].append(text[:10])
    except:
        valueToHandsDict[currentValue] = [text[:10]]
    if text[10] == 'x':
        currentValue = currentValue + 1
    text = f.read(11)
f.close()

print "Creating handToValueDict"
handToValueDict = {}
for value, hands in valueToHandsDict.items():
    for hand in hands:
        handToValueDict[hand] = value
print "Number of hands " + str(len(handToValueDict))


#print "Creating HighToEasyDict"
#f = open("HighToEasyDict.txt", "r")
#text = f.read(22)
#highToEasyDict = {}
#while text != "":
#    highToEasyDict[text[:10]] = [text[11:21]]
#    text = f.read(22)
#f.close()


ext = int(input("Press '1' to get best hand or '0' to exit: "))
while ext == 1:
    cCards = input("Enter Community Cards e.g. '5248444036': ")
    print str(cCards)
    print cCards == 1
    if cCards == 1:
        card1 = str(int(math.ceil(52*random.random())))
        if len(card1) == 1:
            card1 = "0"+card1
        card2 = None
        while card1 == card2 or card2 == None:
            card2 = str(int(math.ceil(52*random.random())))
            if len(card2) == 1:
                card2 = "0"+card2
        card3 = None
        while card1 == card3 or card2 == card3 or card3 == None:
            card3 = str(int(math.ceil(52*random.random())))
            if len(card3) == 1:
                card3 = "0"+card3
        card4 = None
        while card1 == card4 or card2 == card4 or card3 == card4 or card4 == None:
            card4 = str(int(math.ceil(52*random.random())))
            if len(card4) == 1:
                card4 = "0"+card4
        card5 = None        
        while card1 == card5 or card2 == card5 or card3 == card5 or\
        card4 == card5 or card5 == None:
            card5 = str(int(math.ceil(52*random.random())))
            if len(card5) == 1:
                card5 = "0"+card5
        card6 = None        
        while card1 == card6 or card2 == card6 or card3 == card6 \
        or card4 == card6 or card5 == card6 or card6 == None:
            card6 = str(int(math.ceil(52*random.random())))
            if len(card6) == 1:
                card6 = "0"+card6
        card7 = None        
        while card1 == card7 or card2 == card7 or card3 == card7 or card4 == card7\
        or card5 == card7 or card6 == card7 or card7 == None:
            card7 = str(int(math.ceil(52*random.random())))
            if len(card7) == 1:
                card7 = "0"+card7
        print card1
        print card2
        print card3
        print card4
        print card5
        print card6
        print card7
        cCards = card1 + card2 + card3 + card4 + card5
        hCards = card6 + card7
        findBestHand(hCards, cCards)
    else:
        hCards = str(input("Enter Hole Cards e.g. '5150'"))
        findBestHand(hCards, cCards)
        
    ext = int(input("Press '1' to get best hand or '0' to exit: "))
sys.exit()
