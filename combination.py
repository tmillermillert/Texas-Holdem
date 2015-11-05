"""
1100

1010
1001

0110
0101
0011
"""
import sys

def bestHand(sevenCards):
#    print sevenCards
    global handToValueDict
    indexToCard = {}
    start = 0
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
#    print bestHand
    return bestHand

cardBool = [0,0,0,0,0,0,0,0,0,0,\
            0,0,0,0,0,0,0,0,0,0,\
            0,0,0,0,0,0,0,0,0,0,\
            0,0,0,0,0,0,0,0,0,0,\
            0,0,0,0,0,0,0,0,0,0,\
            0,0                  ]
            
print "Creating handToValueDict"    
f = open("handToValueDict.txt", "r")
text = f.read(16)
handToValueDict = {}
while text != "":
    try:
        handToValueDict[text[:10]].append(int(text[11:15]))
    except:
        handToValueDict[text[:10]] = [int(text[11:15])]
    text = f.read(16)
f.close()
print "Finished creating handToValueDict"

boolRange = 47
print boolRange
sevenHandToBestHand = {}
for c1 in range(1,boolRange):
    print "card 1 " + str(c1)
    for c2 in range(c1 + 1, boolRange + 1):
        for c3 in range(c2+ 1, boolRange + 2):
            for c4 in range(c3+1, boolRange + 3):
                for c5 in range(c4+1,boolRange + 4):
                    for c6 in range(c5+1,boolRange + 5):
                        for c7 in range(c6+1,boolRange + 6):
                            if len(str(c1)) < 2:
                                c1s = "0" + str(c1)
                            else:
                                c1s = str(c1)
                            if len(str(c2)) < 2:
                                c2s = "0" + str(c2)
                            else:
                                c2s = str(c2)
                            if len(str(c3)) < 2:
                                c3s = "0" + str(c3)
                            else:
                                c3s = str(c3)
                            if len(str(c4)) < 2:
                                c4s = "0" + str(c4)
                            else:
                                c4s = str(c4)
                            if len(str(c5)) < 2:
                                c5s = "0" + str(c5)
                            else:
                                c5s = str(c5)
                            if len(str(c6)) < 2:
                                c6s = "0" + str(c6)
                            else:
                                c6s = str(c6)
                            if len(str(c7)) < 2:
                                c7s = "0" + str(c7)
                            else:
                                c7s = str(c7)
                            hand = c7s + c6s + c5s + c4s + c3s + c2s + c1s
                            best = bestHand(hand)
                            sevenHandToBestHand[int(hand)] = int(best)
                    
print sys.getsizeof(sevenHandToBestHand)                    
print len(sevenHandToBestHand)
print "52514844403736" + str(sevenHandToBestHand[52514844403736])
print "Finished"
