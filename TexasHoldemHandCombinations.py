from TexasHoldemInclude import cardValueToStr
deck1 = []
for i in range(1,53):
    deck1.append(i)
#print len(deck1)
deck2 = deck1[1:]
#print len(deck2)
deck3 = deck2[1:]
#print len(deck3)
deck4 = deck3[1:]
#print len(deck4)
deck5 = deck4[1:]
#print len(deck5)

#print deck1
#print deck2
#print deck3
#print deck4
#print deck5



hands = set()
for cardValue1 in deck1:
    print len(hands)
    for cardValue2 in deck2:
        for cardValue3 in deck3:
            for cardValue4 in deck4:
                for cardValue5 in deck5:
                    hand = [cardValue1, cardValue2, cardValue3, cardValue4, cardValue5]
                    hand.sort(reverse = True)
                    setHand = set(hand)
                    if len(setHand) < 5:
                        continue
                    #print hand
                    handId = cardValueToStr[hand[0]] + cardValueToStr[hand[1]] +\
                             cardValueToStr[hand[2]] + cardValueToStr[hand[3]] +\
                             cardValueToStr[hand[4]]
                    #print handId
                    handIdLong = long(handId)
                    #print handIdLong
                    hands.add(handIdLong)
                    #break
                #break
            #break
        #break
    #break
#print hands
print "Writing to File"
File = open("hands.txt", "w")
for hand in hands:
    if hand - 1000000000 < 0:
        textHand = "0" + str(hand)
        File.write(textHand)
    else:
        File.write(str(hand))
    File.write(",")
File.close()
print "Finished Writing to file!"

