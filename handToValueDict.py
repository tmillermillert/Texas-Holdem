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

print "writing hand to value dictionary"
f = open("handToValueDict.txt", "w")
for key, value in handToValueDict.items():
    skey = str(key)
    f.write(skey)
    f.write("-")
    svalue = str(value)
    while len(svalue) < 4:
        svalue = "0" + svalue
    f.write(svalue)
    f.write(",")
f.close()
print "Finished"
