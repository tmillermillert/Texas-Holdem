##Find hands with hole cards
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

handHole = []
h1 = "01"
h2 = "50"
for hand in hands:
    if int(hand[0:2]) == int(h1) or int(hand[0:2]) == int(h2):
        handHole.append(hand)
        continue
    if int(hand[2:4]) == int(h1) or int(hand[2:4]) == int(h2):
        handHole.append(hand)
        continue
    if int(hand[4:6]) == h1 or int(hand[4:6]) == int(h2):
        handHole.append(hand)
        continue
    if int(hand[6:8]) == int(h1) or int(hand[6:8]) == int(h2):
        handHole.append(hand)
        continue
    if int(hand[8:10]) == int(h1) or int(hand[8:10]) == int(h2):
        handHole.append(hand)
        continue
        
print "Number of hands with at least 1 hole card " + str(len(handHole))
