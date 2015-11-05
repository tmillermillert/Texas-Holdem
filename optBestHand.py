# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# h h h h h h h h h h -  v  v  v  v  , 
# Hand-Value,   

def eliminateHands(holeCards, communityCards):
    possibleHands = []
    global handToValuesDict
    if communityCards == "00":
        print len(handToValuesDict.keys())
        return handToValuesDict.keys()
    totalValue = 0
    for hand, value in handToValuesDict.items():
        total = 0
        if holeCards[:2] == hand[ :2]  or holeCards[:2] == hand[2:4] or holeCards[:2] == hand[4:6]\
        or holeCards[:2] == hand[6:8]  or holeCards[:2] == hand[8: ]:
            total = total + 1
            
        if holeCards[2:] == hand[ :2] or holeCards[2:] == hand[2:4] or holeCards[2:] == hand[4:6]\
        or holeCards[2:] == hand[6:8] or holeCards[2:] == hand[8: ]:
            total = total + 1
            
        if communityCards[:2] == hand[ :2] or communityCards[:2] == hand[2:4] or communityCards[:2] == hand[4:6] \
        or communityCards[:2] == hand[6:8] or communityCards[:2] == hand[8: ]:
            total = total + 1
            
        if communityCards[2:4] == hand[:2]  or communityCards[2:4] == hand[2:4] or \
        communityCards[2:4] == hand[4:6] or communityCards[2:4] == hand[6:8] \
        or communityCards[2:4] == hand[8:]:
            total = total + 1
            
        if communityCards[4:6] == hand[:2] or communityCards[4:6] == hand[2:4] or \
        communityCards[4:6] == hand[4:6] or communityCards[4:6] == hand[6:8] \
        or communityCards[4:6] == hand[8:]:
            total = total + 1
        
        if len(communityCards) == 6:
            if total >= 3:
                possibleHands.append(hand)
        elif len(communityCards) == 8:
            if communityCards[6:] == hand[:2] or communityCards[6:] == hand[2:4] or \
            communityCards[6:] == hand[4:6] or communityCards[6:] == hand[6:8] \
            or communityCards[6:] == hand[8:]:
                total = total + 1
            if total >= 4:
                possibleHands.append(hand)    
        elif len(communityCards) == 10:
            if communityCards[6:8] == hand[:2] or communityCards[6:8] == hand[2:4] or \
            communityCards[6:8] == hand[4:6] or communityCards[6:8] == hand[6:8] \
            or communityCards[6:8] == hand[8:]:
                total = total + 1
                
            if communityCards[8:] == hand[:2] or communityCards[8:] == hand[2:4] or \
            communityCards[8:] == hand[4:6] or communityCards[8:] == hand[6:8] \
            or communityCards[8:] == hand[8:]:
                total = total + 1   
            if total >= 5:
                print hand
                possibleHands.append(hand)

            
    print len(possibleHands)
    return possibleHands


def opponentHands(holeCards):
    possibleHands = []
    global handToValuesDict
    for hand, value in handToValuesDict.items():
        if holeCards[:2] == hand[ :2]  or holeCards[:2] == hand[2:4] or holeCards[:2] == hand[4:6]\
        or holeCards[:2] == hand[6:8]  or holeCards[:2] == hand[8: ]:
            continue
        if holeCards[2:] == hand[ :2] or holeCards[2:] == hand[2:4] or holeCards[2:] == hand[4:6]\
        or holeCards[2:] == hand[6:8] or holeCards[2:] == hand[8: ]:
            continue
        possibleHands.append(hand)
    print len(possibleHands)
    return possibleHands

print "Creating handToValueDict"    
f = open("handToValueDict.txt", "r")
text = f.read(16)
handToValuesDict = {}
while text != "":
    try:
        handToValuesDict[text[:10]].append(int(text[11:15]))
    except:
        handToValuesDict[text[:10]] = [int(text[11:15])]
    text = f.read(16)
f.close()

holeCards = None
while holeCards == None:
    try:
        holeCards = raw_input("Enter the holecards e.g. 1120 ")
    except:
        holeCards = None
    print holeCards
    try:
        if len(holeCards) % 2 != 0:
            holeCards = None
    except:
        holeCards = None
    try:
        if len(holeCards) < 4:
            holeCards = None
    except:
        holeCards = None
    try:
        if len(holeCards) > 4:
            holeCards = None
    except: 
        holeCards = None
    try:
        int(holeCards)
    except:
        holeCards = None
    
communityCards = None        
while communityCards == None:
    try:
        communityCards = raw_input("Enter the communitycards e.g. 0 or 112022 or 12202213 or 1220221352: ")
    except:
        communityCards = None
    print communityCards
    try:
        if len(communityCards) % 2 != 0:
            communityCards = None
    except:
        communityCards = None
    if communityCards == "00":
        break
    try:
        if len(communityCards) > 10 or len(communityCards) < 6:
            communityCards = None 
    except:
        communityCards = None 
        
potSize   = raw_input("Enter the pot size ")
minBet    = raw_input("Enter the minimum bet ")
opponentHands(holeCards)
#eliminateHands(holeCards, communityCards)
