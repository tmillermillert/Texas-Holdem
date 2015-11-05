print "Creating valueToHandsDict"    
f = open("highOrderedHands.txt", "r")
text = f.read(11)
currentValue = 0
valueToHandsDict = {}
numHands = 0.0
while text != "":
    numHands = numHands + 1
    try:
        valueToHandsDict[currentValue].append(text[:10])
    except:
        valueToHandsDict[currentValue] = [text[:10]]
    if text[10] == 'x':
        currentValue = currentValue + 1
    text = f.read(11)
f.close()
continuous = 0
#for key, value in valueToHandsDict.items():
#    print str(key) + " " + str(len(value))
    
#for key, value in valueToHandsDict.items():
#    continuous = continuous + len(value)
#    print str(key) + " " + str(continuous)
    
#for key, value in valueToHandsDict.items():
#    continuous = continuous + len(value)
#    print str(key) + " " + str(continuous / numHands)

for key, value in valueToHandsDict.items():
    print str(key) + " " + str(len(value) / numHands)
