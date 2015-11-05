import sys

def bestHand(sevenCards):
    #print "x"
    #print sevenCards
    global handToValueDict
    indexToCard = {}
    cardsList = []
    for i in range(0,14):
        #print i
        if i % 2 == 0:
            cardsList.append(sevenCards[i:i+2])
        
    cardsList.sort(reverse = True)
    #print cardsList
    #print len(cardsList)
    sevenCards = cardsList[0] + cardsList[1] + cardsList[2] + cardsList[3] +\
    cardsList[4] + cardsList[5] + cardsList[6]
    start = 0
    #print "seven cards = " + str(sevenCards)
    for i in range(7):
        indexToCard[i] = sevenCards[start:start+2]
        start = start + 2
    boolRange = 2
    bestHand = sevenCards[:10]
    bestHandValue = handToValueDict[bestHand]
    for c1 in range(boolRange):
        for c2 in range(c1 + 1, boolRange + 1):
            for c3 in range(c2+ 1, boolRange + 2):
                for c4 in range(c3+1, boolRange + 3):
                    for c5 in range(c4+1,boolRange + 4):
                        hand = indexToCard[c1] + indexToCard[c2]\
                        + indexToCard[c3] + indexToCard[c4]\
                        + indexToCard[c5]
                        if handToValueDict[hand] > bestHandValue:
                            bestHand = hand
                            bestHandValue = handToValueDict[hand]
                            
    print "seven cards: " + str(sevenCards) + " , seven cards value: " + str(bestHandValue)
    return bestHandValue


#########################################################################




print "Creating handToValueDict"    
f = open("handToValueDict.txt", "r")
text = f.read(16)
handToValueDict = {}
while text != "":
    handToValueDict[text[:10]] = int(text[11:15])
    text = f.read(16)
f.close()
print "Finished creating handToValueDict"

boolRange = 52
print "Creating two card combinations"
twoCardCombinations = []
for c1 in range(1,boolRange):
    for c2 in range(c1 + 1, boolRange+1):
        if len(str(c2)) == 1:
            if len(str(c1)) == 1:
                twoCardCombinations.append("0" + str(c2) + "0" + str(c1))
            else:
                twoCardCombinations.append("0" + str(c2) + str(c1))
        else:
            if len(str(c1)) == 1:
                twoCardCombinations.append(str(c2) + "0" + str(c1))
            else:
                twoCardCombinations.append(str(c2) + str(c1))
               
print "Number of two pair combinations " + str(len(twoCardCombinations))

print "Creating seven cards combinations"
cards = ["01","02","03","04","05","06","07","08","09","10","11","12","13",\
         "14","15","16","17","18","19","20","21","22","23","24","25","26",\
         "27","28","29","30","31","32","33","34","35","36","37","38","39",\
         "40","41","42","43","44","45","46","47","48","49","50","51","52"]
         
cardsCopy = cards[:]
         
boolRange = 8
sevenHandToBestHand = {}
for twoCards in twoCardCombinations: 
    cardsCopy = cards[:]
    ind1 = cardsCopy.index(twoCards[:2])
    ind2 = cardsCopy.index(twoCards[2:])
    cardsCopy.pop(ind1)
    cardsCopy.pop(ind2)
    indexToCard = {}
    for i in range(1,51):
        indexToCard[i] = cardsCopy.pop()
    
    for c1 in range(1,boolRange):
        for c2 in range(c1 + 1, boolRange + 1):
            for c3 in range(c2+ 1, boolRange + 2):
                for c4 in range(c3+1, boolRange + 3):
                    for c5 in range(c4+1,boolRange + 4):
                        sevenCards = twoCards + indexToCard[c5] + indexToCard[c4] +\
                        indexToCard[c3] + indexToCard[c2] + indexToCard[c1]
                        #print "Inner combo " + str(sevenCards)
                        best = bestHand(sevenCards)
                        sevenHandToBestHand[sevenCards] = best

print "Number of seven card combinations " + str(len(sevenHandToBestHand))
                        
