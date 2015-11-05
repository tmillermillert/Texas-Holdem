from TexasHoldemInclude import card
from TexasHoldemInclude import cardValueToCard
from TexasHoldemInclude import cardValueToStr
from TexasHoldemInclude import cardValueDict
from TexasHoldemInclude import cardToValue
from TexasHoldemInclude import cardToStrValue
import math

totalValues = 0

hands = []
f = open("hands.txt", "r")
text = f.read(11)
while text != "":
    text = text[:10]
    hands.append(text)
    text = f.read(11)
f.close()
num_hands = len(hands)
print "Number of Hands loaded " + str(num_hands)

print "Creating highOrderToEasyDict"
highCardValueToHandsDict = {}
for hand in hands:
    card1 = cardValueToCard[int(hand[8:10])]
    card2 = cardValueToCard[int(hand[6:8])]
    card3 = cardValueToCard[int(hand[4:6])]
    card4 = cardValueToCard[int(hand[2:4])]
    card5 = cardValueToCard[int(hand[0:2])]
    
    if card1.rank == card2.rank or card2.rank == card3.rank or card3.rank == card4.rank\
       or card4.rank == card5.rank:
        continue
    elif card1.suit == card2.suit == card3.suit == card4.suit == card5.suit:
        continue
    elif card1.rank + 4 == card2.rank + 3 == card3.rank + 2 == card4.rank + 1\
        == card5.rank:
        continue
    elif card5.rank == 14 and card1.rank + 3 == card2.rank + 2 == card3.rank + 1\
         == card4.rank and card1.rank == 2:
        continue
    else:
        highCardValueToHandsDict[hand] = hand
print "Number of items in highCardValueToHandsDict " + str(len(highCardValueToHandsDict))  

adjustedValueToHandsDict = {}
print "Updating mainDict"
adjustedValueToHandsDict.update(highCardValueToHandsDict)

highCardValueToHandsDict = None

print "Creating onePairHighToEasyDict"
onePairValueToHandsDict = {}
for hand in hands:
    card5 = cardValueToCard[int(hand[8:10])]
    card4 = cardValueToCard[int(hand[6:8])]
    card3 = cardValueToCard[int(hand[4:6])]
    card2 = cardValueToCard[int(hand[2:4])]
    card1 = cardValueToCard[int(hand[0:2])]
    
    if card1.rank == card2.rank == card3.rank or card3.rank == card4.rank == card5.rank:
        continue
    elif card2.rank == card3.rank == card4.rank:
        continue
    elif card1.rank == card2.rank and card3.rank == card4.rank:
        continue
    elif card1.rank == card2.rank and card4.rank == card5.rank:
        continue
    elif card2.rank == card3.rank and card4.rank == card5.rank:
        continue
    elif card1.rank == card2.rank:
        onePairValueToHandsDict[hand] = hand[:4] + hand[4:]
    elif card2.rank == card3.rank:
        onePairValueToHandsDict[hand] = hand[2:6] + hand[:2] + hand[6:]
    elif card3.rank == card4.rank:
        onePairValueToHandsDict[hand] = hand[4:8] + hand[:4] + hand[8:]
    elif card4.rank == card5.rank:
        onePairValueToHandsDict[hand] = hand[6:] + hand[:6]
print "Number of items in onePairHighToEasyDict " + str(len(onePairValueToHandsDict))        

print "Updating mainDict"
adjustedValueToHandsDict.update(onePairValueToHandsDict)

onePairValueToHandsDict = None

print "Creating twoPairHighToEasyDict"    
twoPairValueToHandsDict = {}
for hand in hands:
    card5 = cardValueToCard[int(hand[8:10])]
    card4 = cardValueToCard[int(hand[6:8])]
    card3 = cardValueToCard[int(hand[4:6])]
    card2 = cardValueToCard[int(hand[2:4])]
    card1 = cardValueToCard[int(hand[0:2])]
    if card1.rank == card2.rank == card3.rank or card3.rank == card4.rank == card5.rank:
        continue
    elif card1.rank == card2.rank:
        if card3.rank == card4.rank:
            twoPairValueToHandsDict[hand] = hand[:8] + hand[8:]
        elif card4.rank == card5.rank:
            twoPairValueToHandsDict[hand] = hand[:4] + hand[6:] + hand[4:6]
    elif card2.rank == card3.rank:
        if card4.rank == card5.rank:
            twoPairValueToHandsDict[hand] = hand[2:] + hand[0:2]
print "Number of items in twoPairHighToEasyDict " + str(len(twoPairValueToHandsDict))

print "Updating mainDict"
adjustedValueToHandsDict.update(twoPairValueToHandsDict)

twoPairValueToHandsDict = None

print "Creating threeOfAKindHighToEasyDict"  
threeOfAKindValueToHandsDict = {}
for hand in hands:
    card5 = cardValueToCard[int(hand[8:10])]
    card4 = cardValueToCard[int(hand[6:8])]
    card3 = cardValueToCard[int(hand[4:6])]
    card2 = cardValueToCard[int(hand[2:4])]
    card1 = cardValueToCard[int(hand[0:2])]
    
    if card1.rank == card2.rank == card3.rank:
        if card4.rank == card5.rank or card3.rank == card4.rank:
            continue
        else:
            threeOfAKindValueToHandsDict[hand] = hand
    elif card3.rank == card4.rank == card5.rank:
        if card1.rank == card2.rank or card2.rank == card3.rank:
            continue
        else:
            threeOfAKindValueToHandsDict[hand] = hand[4:] + hand[:4]
    elif card2.rank == card3.rank == card4.rank:
        if card1.rank == card2.rank or card4.rank == card5.rank:
            continue
        else:
            threeOfAKindValueToHandsDict[hand] = hand[2:8] + hand[:2] + hand[8:] 
print "Number of items in threeOfAKindHighToEasyDict " + str(len(threeOfAKindValueToHandsDict))

print "Updating mainDict"
adjustedValueToHandsDict.update(threeOfAKindValueToHandsDict)

threeOfAKindValueToHandsDict = None
   
print "Creating straightValueToHandsDict" 
straightValueToHandsDict = {}
for hand in hands:
    card1 = cardValueToCard[int(hand[8:10])]
    card2 = cardValueToCard[int(hand[6:8])]
    card3 = cardValueToCard[int(hand[4:6])]
    card4 = cardValueToCard[int(hand[2:4])]
    card5 = cardValueToCard[int(hand[0:2])]
    
    if card1.rank+4 == card2.rank+3 == card3.rank+2 == card4.rank+1 == card5.rank:
        if card1.suit == card2.suit == card3.suit == card4.suit == card5.suit:
            continue
        else:
            straightValueToHandsDict[hand] = hand
    else:
        if card5.rank == 14:
            if card1.rank == 2:
                if card1.rank+3 == card2.rank+2 == card3.rank+1 == card4.rank:
                    if card1.suit == card2.suit == card3.suit == card4.suit == card5.suit:
                        continue
                    else:
                        straightValueToHandsDict[hand] = hand[2:]+hand[0:2]
print "Number of items in straightHighToEasyDict " + str(len(straightValueToHandsDict))

print "Updating mainDict"
adjustedValueToHandsDict.update(straightValueToHandsDict)

straightValueToHandsDict = None                            

print "Creating flushHighToEasyDict"
flushValueToHandsDict = {}
for hand in hands:
    card1 = cardValueToCard[int(hand[8:10])]
    card2 = cardValueToCard[int(hand[6:8])]
    card3 = cardValueToCard[int(hand[4:6])]
    card4 = cardValueToCard[int(hand[2:4])]
    card5 = cardValueToCard[int(hand[0:2])]
    
    if card1.suit == card2.suit == card3.suit == card4.suit == card5.suit:
        if card1.rank+4 == card2.rank+3 == card3.rank+2 == card4.rank+1 == card5.rank:
            continue
        elif card5.rank == 14:
            if card1.rank == 2:
                if card1.rank+3 == card2.rank+2 == card3.rank+1 == card4.rank:        
                    continue
                else:
                    flushValueToHandsDict[hand] = hand
            else:
                flushValueToHandsDict[hand] = hand
        else:
            flushValueToHandsDict[hand] = hand
print "Number of items in flushHighToEasyDict " + str(len(flushValueToHandsDict))

print "Updating mainDict"
adjustedValueToHandsDict.update(flushValueToHandsDict)

flushValueToHandsDict = None 

print "Creating fullHouseValueToHandsDict"
fullHouseValueToHandsDict = {}
for hand in hands:
    card1 = cardValueToCard[int(hand[8:10])]
    card2 = cardValueToCard[int(hand[6:8])]
    card3 = cardValueToCard[int(hand[4:6])]
    card4 = cardValueToCard[int(hand[2:4])]
    card5 = cardValueToCard[int(hand[0:2])]
    
    if card1.rank == card2.rank == card3.rank:
        if card4.rank == card5.rank:
            fullHouseValueToHandsDict[hand] = hand[4:] + hand[:4]
    elif card5.rank == card4.rank == card3.rank:
        if card1.rank == card2.rank:
            fullHouseValueToHandsDict[hand] = hand
print "Number of items in fullHouseHighToEasyDict " + str(len(fullHouseValueToHandsDict))

print "Updating mainDict"
adjustedValueToHandsDict.update(fullHouseValueToHandsDict)

fullHouseValueToHandsDict = None 

print "Creating fourOfAKindHighToEasyDict"
fourOfAKindValueToHandsDict = {}
for hand in hands:
    card1 = cardValueToCard[int(hand[8:10])]
    card2 = cardValueToCard[int(hand[6:8])]
    card3 = cardValueToCard[int(hand[4:6])]
    card4 = cardValueToCard[int(hand[2:4])]
    card5 = cardValueToCard[int(hand[0:2])]
    if card1.rank == card2.rank == card3.rank == card4.rank:
        fourOfAKindValueToHandsDict[hand] = hand[2:] + hand[:2]
    elif card2.rank == card3.rank == card4.rank == card5.rank:
        fourOfAKindValueToHandsDict[hand] = hand
print "Number of items in fourOfAKindHighToEasyDict " + str(len(fourOfAKindValueToHandsDict))

print "Updating mainDict"
adjustedValueToHandsDict.update(fourOfAKindValueToHandsDict)

fourOfAKindValueToHandsDict = None

print "Creating straightFlushHighToEasyDict"
straightFlushValueToHandsDict = {}
for hand in hands:
    card1 = cardValueToCard[int(hand[8:10])]
    card2 = cardValueToCard[int(hand[6:8])]
    card3 = cardValueToCard[int(hand[4:6])]
    card4 = cardValueToCard[int(hand[2:4])]
    card5 = cardValueToCard[int(hand[0:2])]
    if card1.suit == card2.suit == card3.suit == card4.suit == card5.suit:
        if card1.rank+4 == card2.rank+3 == card3.rank+2 == card4.rank+1 == card5.rank:
            straightFlushValueToHandsDict[hand] = hand
        else:
            if card5.rank == 14:
                if card1.rank == 2:
                    if card1.rank+3 == card2.rank+2 == card3.rank+1 == card4.rank:
                        straightFlushValueToHandsDict[hand] = hand[2:] + hand[:2]
print "Number of items in straightFlushHighToEasyDict " + \
str(len(straightFlushValueToHandsDict))

print "Updating mainDict"
adjustedValueToHandsDict.update(straightFlushValueToHandsDict)

straightFlushValueToHandsDict = None

print str(len(adjustedValueToHandsDict)) + " keys in adjustedValueToHandsDict"                     
print str(len(adjustedValueToHandsDict.values())) + " values in adjustedValueToHandsDict" 

print "Writing to HighToEasyDict.txt"
File = open("HighToEasyDict.txt", "w")
for key, value in adjustedValueToHandsDict.iteritems():
    File.write(key)
    File.write(">")
    File.write(value)
    File.write("x")
File.close()
print "Finished"

