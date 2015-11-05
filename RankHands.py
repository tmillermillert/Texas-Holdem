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

print "Creating highCardValueToHandsDict"
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
        try:
            highCardValueToHandsDict[15000*card5.rank + 1500*card4.rank + 150*card3.rank\
            + 15*card2.rank + card1.rank].append(hand)
        except:
            highCardValueToHandsDict[15000*card5.rank + 1500*card4.rank + 150*card3.rank\
            + 15*card2.rank + card1.rank] = [hand]
print "Number of items in highCardValueToHandsDict " + str(len(highCardValueToHandsDict))  

highCardValueList = highCardValueToHandsDict.keys()
print "Sorting highCardValueToHandsDict keys"
highCardValueList.sort()

adjustedValueToHandsDict = {}
print "Normalizing value keys from highCardValueToHandsDict to adjustedValueToHandsDict"
for i in range(len(highCardValueList)):
    adjustedValueToHandsDict[i] = highCardValueToHandsDict[highCardValueList[i]]

highCardValueToHandsDict = None
highCardValueList = None

print "Creating onePairValueToHandsDict"
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
        try:
            onePairValueToHandsDict[(17000*card1.rank) + (150*card3.rank) + (13*card4.rank)\
            + card5.rank].append(hand[:4] + hand[4:])
        except:
            onePairValueToHandsDict[(17000*card1.rank) + (150*card3.rank) + (13*card4.rank)\
            + card5.rank] = [hand[:4] + hand[4:]]
    elif card2.rank == card3.rank:
        try:
            onePairValueToHandsDict[(17000*card2.rank) + (150*card1.rank) + (13*card4.rank)\
            + card5.rank].append(hand[2:6] + hand[:2] + hand[6:])
        except:
            onePairValueToHandsDict[(17000*card2.rank) + (150*card1.rank) + (13*card4.rank)\
            + card5.rank] = [hand[2:6] + hand[:2] + hand[6:]]
    elif card3.rank == card4.rank:
        try:
            onePairValueToHandsDict[(17000*card3.rank) + (150*card1.rank) + (13*card2.rank)\
            + card5.rank].append(hand[4:8] + hand[:4] + hand[8:])
        except:
            onePairValueToHandsDict[(17000*card3.rank) + (150*card1.rank) + (13*card2.rank)\
            + card5.rank] = [hand[4:8] + hand[:4] + hand[8:]]
    elif card4.rank == card5.rank:
        try:
            onePairValueToHandsDict[(17000*card4.rank) + (150*card1.rank) + (13*card2.rank)\
            + card3.rank].append(hand[6:] + hand[:6])
        except:
            onePairValueToHandsDict[(17000*card4.rank) + (150*card1.rank) + (13*card2.rank)\
            + card3.rank] = [hand[6:] + hand[:6]]
print "Number of items in onePairValueToHandsDict " + str(len(onePairValueToHandsDict))        
 
onePairValueList = onePairValueToHandsDict.keys()
print "Sorting onePairValueToHandsDict keys"
onePairValueList.sort()

adjustedIndex = len(adjustedValueToHandsDict)
print "Normalizing value keys from onePairValueToHandsDict to adjustedValueToHandsDict"
for i in range(len(onePairValueList)):
    adjustedValueToHandsDict[adjustedIndex+i] = onePairValueToHandsDict[onePairValueList[i]]  

onePairValueList = None
onePairValueToHandsDict = None

print "Creating twoPairValueToHandsDict"    
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
            try:
                twoPairValueToHandsDict[(150*card1.rank) + (13*card3.rank) + card5.rank]\
                .append(hand[:8] + hand[8:])
            except:
                twoPairValueToHandsDict[(150*card1.rank) + (13*card3.rank) + card5.rank]\
                = [hand[:8] + hand[8:]]
        elif card4.rank == card5.rank:
            try:
                twoPairValueToHandsDict[(150*card1.rank) + (13*card4.rank) + card3.rank]\
                .append(hand[:4] + hand[6:] + hand[4:6])
            except:
                twoPairValueToHandsDict[(150*card1.rank) + (13*card4.rank) + card3.rank]\
                = [hand[:4] + hand[6:] + hand[4:6]]
    elif card2.rank == card3.rank:
        if card4.rank == card5.rank:
            try:
                twoPairValueToHandsDict[(150*card2.rank) + (13*card4.rank) + card1.rank]\
                .append(hand[2:] + hand[0:2])
            except:
                twoPairValueToHandsDict[(150*card2.rank) + (13*card4.rank) + card1.rank]\
                = [hand[2:] + hand[0:2]]
print "Number of items in twoPairValueToHandsDict " + str(len(twoPairValueToHandsDict))

twoPairValueList = twoPairValueToHandsDict.keys()
print "Sorting twoPairValueToHandsDict keys"
twoPairValueList.sort()

adjustedIndex = len(adjustedValueToHandsDict)
print "Normalizing value keys from twoPairValueToHandsDict to adjustedValueToHandsDict"
for i in range(len(twoPairValueList)):
    adjustedValueToHandsDict[adjustedIndex+i] = twoPairValueToHandsDict[twoPairValueList[i]] 

twoPairValueList = None
twoPairValueToHandsDict = None

print "Creating threeOfAKindValueToHandsDict"  
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
            try:
                threeOfAKindValueToHandsDict[card1.rank * 1000 + card4.rank * 15 + card5.rank]\
                .append(hand)
            except:
                threeOfAKindValueToHandsDict[card1.rank * 1000 + card4.rank * 15 + card5.rank]\
                 = [hand]
    elif card3.rank == card4.rank == card5.rank:
        if card1.rank == card2.rank or card2.rank == card3.rank:
            continue
        else:
            try:
                threeOfAKindValueToHandsDict[card3.rank * 1000 + card1.rank * 15 + card2.rank]\
                .append(hand[4:] + hand[:4])
            except:
                threeOfAKindValueToHandsDict[card3.rank * 1000 + card1.rank * 15 + card2.rank] = \
                [hand[4:] + hand[:4]]
    elif card2.rank == card3.rank == card4.rank:
        if card1.rank == card2.rank or card4.rank == card5.rank:
            continue
        else:
            try:
                threeOfAKindValueToHandsDict[card2.rank * 1000 + card1.rank * 15 + card5.rank]\
                .append(hand[2:8] + hand[:2] + hand[8:])
            except:
                threeOfAKindValueToHandsDict[card2.rank * 1000 + card1.rank * 15 + card5.rank] =\
                [hand[2:8] + hand[:2] + hand[8:]]  
print "Number of items in threeOfAKindValueToHandsDict " + str(len(threeOfAKindValueToHandsDict))

threeOfAKindValueList = threeOfAKindValueToHandsDict.keys()
print "Sorting threeOfAKindValueToHandsDict keys"
threeOfAKindValueList.sort()

adjustedIndex = len(adjustedValueToHandsDict)
print "Normalizing value keys from threeOfAKindValueToHandsDict to adjustedValueToHandsDict"
for i in range(len(threeOfAKindValueList)):
    adjustedValueToHandsDict[adjustedIndex+i] = threeOfAKindValueToHandsDict\
    [threeOfAKindValueList[i]] 

threeOfAKindValueList = None
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
            try:
                straightValueToHandsDict[card5.rank].append(hand)
            except:
                straightValueToHandsDict[card5.rank] = [hand]
    else:
        if card5.rank == 14:
            if card1.rank == 2:
                if card1.rank+3 == card2.rank+2 == card3.rank+1 == card4.rank:
                    if card1.suit == card2.suit == card3.suit == card4.suit == card5.suit:
                        continue
                    else:
                        try:
                            straightValueToHandsDict[card4.rank].append(hand[2:]+hand[0:2])
                        except:
                            straightValueToHandsDict[card4.rank] = [hand[2:]+hand[0:2]]
print "Number of items in straightValueToHandsDict " + str(len(straightValueToHandsDict))

straightValueList = straightValueToHandsDict.keys()
print "Sorting straightValueToHandsDict keys"
straightValueList.sort()

adjustedIndex = len(adjustedValueToHandsDict)
print "Normalizing value keys from straightValueToHandsDict to adjustedValueToHandsDict"
for i in range(len(straightValueList)):
    adjustedValueToHandsDict[adjustedIndex+i] = straightValueToHandsDict\
    [straightValueList[i]] 

straightValueList = None
straightValueToHandsDict = None                            

print "Creating flushValueToHandsDict"
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
                    try:
                        flushValueToHandsDict[15000*card5.rank + 1500*card4.rank + \
                        150*card3.rank + 15*card2.rank + card1.rank].append(hand)
                    except:
                        flushValueToHandsDict[15000*card5.rank + 1500*card4.rank + \
                        150*card3.rank + 15*card2.rank + card1.rank] = [hand]
            else:
                try:
                    flushValueToHandsDict[15000*card5.rank + 1500*card4.rank + \
                    150*card3.rank + 15*card2.rank + card1.rank].append(hand)
                except:
                    flushValueToHandsDict[15000*card5.rank + 1500*card4.rank + \
                    150*card3.rank + 15*card2.rank + card1.rank] = [hand]
        else:
            try:
                flushValueToHandsDict[15000*card5.rank + 1500*card4.rank + \
                150*card3.rank + 15*card2.rank + card1.rank].append(hand)
            except:
                flushValueToHandsDict[15000*card5.rank + 1500*card4.rank + \
                150*card3.rank + 15*card2.rank + card1.rank] = [hand]
print "Number of items in flushValueToHandsDict " + str(len(flushValueToHandsDict))

flushValueList = flushValueToHandsDict.keys()
print "Sorting flushValueToHandsDict keys"
flushValueList.sort()

adjustedIndex = len(adjustedValueToHandsDict)
print "Normalizing value keys from flushValueToHandsDict to adjustedValueToHandsDict"
for i in range(len(flushValueList)):
    adjustedValueToHandsDict[adjustedIndex+i] = flushValueToHandsDict\
    [flushValueList[i]] 

flushValueList = None
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
            try:
                fullHouseValueToHandsDict[card1.rank * 15 + card4.rank].append(hand[4:]\
                + hand[:4])
            except:
                fullHouseValueToHandsDict[card1.rank * 15 + card4.rank] = [hand[4:]\
                + hand[:4]]
    elif card5.rank == card4.rank == card3.rank:
        if card1.rank == card2.rank:
            try:
                fullHouseValueToHandsDict[card3.rank * 15 + card1.rank].append(hand)
            except:
                fullHouseValueToHandsDict[card3.rank * 15 + card1.rank] = [hand]
print "Number of items in fullHouseValueToHandsDict " + str(len(fullHouseValueToHandsDict))

fullHouseValueList = fullHouseValueToHandsDict.keys()
print "Sorting fullHouseValueToHandsDict keys"
fullHouseValueList.sort()

adjustedIndex = len(adjustedValueToHandsDict)
print "Normalizing value keys from fullHouseValueToHandsDict to adjustedValueToHandsDict"
for i in range(len(fullHouseValueList)):
    adjustedValueToHandsDict[adjustedIndex+i] = fullHouseValueToHandsDict\
    [fullHouseValueList[i]] 

fullHouseValueList = None
fullHouseValueToHandsDict = None 

print "Creating fourOfAKindValueToHandsDict"
fourOfAKindValueToHandsDict = {}
for hand in hands:
    card1 = cardValueToCard[int(hand[8:10])]
    card2 = cardValueToCard[int(hand[6:8])]
    card3 = cardValueToCard[int(hand[4:6])]
    card4 = cardValueToCard[int(hand[2:4])]
    card5 = cardValueToCard[int(hand[0:2])]
    if card1.rank == card2.rank == card3.rank == card4.rank:
        try:
            fourOfAKindValueToHandsDict[card1.rank * 15 + card5.rank]\
            .append(hand[2:] + hand[:2])
        except:
            fourOfAKindValueToHandsDict[card1.rank * 15 + card5.rank] = \
            [hand[2:] + hand[:2]]
    elif card2.rank == card3.rank == card4.rank == card5.rank:
        try:
            fourOfAKindValueToHandsDict[card2.rank * 15 + card1.rank]\
            .append(hand)
        except:
            fourOfAKindValueToHandsDict[card2.rank * 15 + card1.rank] = \
            [hand]
print "Number of items in fourOfAKindValueToHandsDict " + str(len(fourOfAKindValueToHandsDict))

fourOfAKindValueList = fourOfAKindValueToHandsDict.keys()
print "Sorting fourOfAKindValueToHandsDict keys"
fourOfAKindValueList.sort()

adjustedIndex = len(adjustedValueToHandsDict)
print "Normalizing value keys from fourOfAKindValueToHandsDict to adjustedValueToHandsDict"
for i in range(len(fourOfAKindValueList)):
    adjustedValueToHandsDict[adjustedIndex+i] = fourOfAKindValueToHandsDict\
    [fourOfAKindValueList[i]] 

fourOfAKindValueList = None
fourOfAKindValueToHandsDict = None

print "Creating straightFlushValueToHandsDict"
straightFlushValueToHandsDict = {}
for hand in hands:
    card1 = cardValueToCard[int(hand[8:10])]
    card2 = cardValueToCard[int(hand[6:8])]
    card3 = cardValueToCard[int(hand[4:6])]
    card4 = cardValueToCard[int(hand[2:4])]
    card5 = cardValueToCard[int(hand[0:2])]
    if card1.suit == card2.suit == card3.suit == card4.suit == card5.suit:
        if card1.rank+4 == card2.rank+3 == card3.rank+2 == card4.rank+1 == card5.rank:
            try:
                straightFlushValueToHandsDict[card5.rank].append(hand)
            except:
                straightFlushValueToHandsDict[card5.rank] = [hand]
        else:
            if card5.rank == 14:
                if card1.rank == 2:
                    if card1.rank+3 == card2.rank+2 == card3.rank+1 == card4.rank:
                        try:
                            straightFlushValueToHandsDict[card4.rank].append(hand[2:] + hand[:2])
                        except:
                            straightFlushValueToHandsDict[card4.rank] = [hand[2:] + hand[:2]]
print "Number of items in straightFlushValueToHandsDict " + \
str(len(straightFlushValueToHandsDict))

straightFlushValueList = straightFlushValueToHandsDict.keys()
print "Sorting straightFlushValueToHandsDict keys"
straightFlushValueList.sort()

adjustedIndex = len(adjustedValueToHandsDict)
print "Normalizing value keys from straightFlushValueToHandsDict to adjustedValueToHandsDict"
for i in range(len(straightFlushValueList)):
    adjustedValueToHandsDict[adjustedIndex+i] = straightFlushValueToHandsDict\
    [straightFlushValueList[i]] 

straightFlushValueList = None
straightFlushValueToHandsDict = None

print str(len(adjustedValueToHandsDict)) + " keys in adjustedValueToHandsDict"                     

print "Writing to OrderedHands.txt"
File = open("OrderedHands.txt", "w")
for handIndex in range(len(adjustedValueToHandsDict)):
    listOfHandsWithSameValue = adjustedValueToHandsDict[handIndex]
    for hand in listOfHandsWithSameValue:
        File.write(hand)
        File.write(",")
    File.seek(-1,1)
    File.write("x")
File.close()
print "Finished"

