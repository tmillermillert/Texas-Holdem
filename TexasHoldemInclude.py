ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = [1, 2, 3, 4]
suitToStrDict ={4:"Spades",3:"Hearts",2:"Clubs",1:"Diamonds"}
rankToStrDict = {2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",\
                 10:"Ten",11:"Jack",12:"Queen",13:"King",14:"Ace"}
cardValueDict = {"Two of Diamonds"  : 1, "Two of Clubs"   : 2,\
                 "Two of Hearts"    : 3, "Two of Spades"  : 4,\
                 "Three of Diamonds": 5, "Three of Clubs" : 6,\
                 "Three of Hearts"  : 7, "Three of Spades": 8,\
                 "Four of Diamonds" : 9, "Four of Clubs"  :10,\
                 "Four of Hearts"   :11, "Four of Spades" :12,\
                 "Five of Diamonds" :13, "Five of Clubs"  :14,\
                 "Five of Hearts"   :15, "Five of Spades" :16,\
                 "Six of Diamonds"  :17, "Six of Clubs"   :18,\
                 "Six of Hearts"    :19, "Six of Spades"  :20,\
                 "Seven of Diamonds":21, "Seven of Clubs" :22,\
                 "Seven of Hearts"  :23, "Seven of Spades":24,\
                 "Eight of Diamonds":25, "Eight of Clubs" :26,\
                 "Eight of Hearts"  :27, "Eight of Spades":28,\
                 "Nine of Diamonds" :29, "Nine of Clubs"  :30,\
                 "Nine of Hearts"   :31, "Nine of Spades" :32,\
                 "Ten of Diamonds"  :33, "Ten of Clubs"   :34,\
                 "Ten of Hearts"    :35, "Ten of Spades"  :36,\
                 "Jack of Diamonds" :37, "Jack of Clubs"  :38,\
                 "Jack of Hearts"   :39, "Jack of Spades" :40,\
                 "Queen of Diamonds":41, "Queen of Clubs" :42,\
                 "Queen of Hearts"  :43, "Queen of Spades":44,\
                 "King of Diamonds" :45, "King of Clubs"  :46,\
                 "King of Hearts"   :47, "King of Spades" :48,\
                 "Ace of Diamonds"  :49, "Ace of Clubs"   :50,\
                 "Ace of Hearts"    :51, "Ace of Spades"  :52 }
                 
class card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __cmp__(self, other):
        if cardValueDict[str(self)] < cardValueDict[str(other)]:
            return -1
        elif cardValueDict[str(self)] < cardValueDict[str(other)]:
            return 0
        else:
            return 1
    def __str__(self):
        return rankToStrDict[self.rank] + " of " + suitToStrDict[self.suit]  
class makeHand:
    def __init__(self, card1, card2, card3, card4, card5):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4
        self.card5 = card5

def makeDeck():
    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append(card(rank, suit))
    return deck
def printVHand(hVal):
    hhand = []
    iHVal = int(hVal)
    while  iHVal > 0:
        remaider = iHVal % 100
        iHVal = iHVal/100
        hVcard = cardValueToCard[remaider]
        hhand.append(hVcard)
    printHand(hhand)
def printDeck(deck):
    for card in deck:
        printCard(card)
def printCard(card):
    print rankToStrDict[card.rank] + " of " + suitToStrDict[card.suit]
cardValueToCard = {1 :  card(2,1), 2 :  card(2,2),\
                   3 :  card(2,3), 4 :  card(2,4),\
                   5 :  card(3,1), 6 :  card(3,2),\
                   7 :  card(3,3), 8 :  card(3,4),\
                   9 :  card(4,1), 10:  card(4,2),\
                   11:  card(4,3), 12:  card(4,4),\
                   13:  card(5,1), 14:  card(5,2),\
                   15:  card(5,3), 16:  card(5,4),\
                   17:  card(6,1), 18:  card(6,2),\
                   19:  card(6,3), 20:  card(6,4),\
                   21:  card(7,1), 22:  card(7,2),\
                   23:  card(7,3), 24:  card(7,4),\
                   25:  card(8,1), 26:  card(8,2),\
                   27:  card(8,3), 28:  card(8,4),\
                   29:  card(9,1), 30:  card(9,2),\
                   31:  card(9,3), 32:  card(9,4),\
                   33: card(10,1), 34: card(10,2),\
                   35: card(10,3), 36: card(10,4),\
                   37: card(11,1), 38: card(11,2),\
                   39: card(11,3), 40: card(11,4),\
                   41: card(12,1), 42: card(12,2),\
                   43: card(12,3), 44: card(12,4),\
                   45: card(13,1), 46: card(13,2),\
                   47: card(13,3), 48: card(13,4),\
                   49: card(14,1), 50: card(14,2),\
                   51: card(14,3), 52: card(14,4) }
cardValueToStr = {1 :"01", 2: "02",3 :"03",4 :"04",5 :"05",\
                  6 :"06", 7: "07",8 :"08",9 :"09",10:"10",\
                  11:"11", 12:"12",13:"13",14:"14",15:"15",\
                  16:"16", 17:"17",18:"18",19:"19",20:"20",\
                  21:"21", 22:"22",23:"23",24:"24",25:"25",\
                  26:"26", 27:"27",28:"28",29:"29",30:"30",\
                  31:"31", 32:"32",33:"33",34:"34",35:"35",\
                  36:"36", 37:"37",38:"38",39:"39",40:"40",\
                  41:"41", 42:"42",43:"43",44:"44",45:"45",\
                  46:"46", 47:"47",48:"48",49:"49",50:"50",\
                  51:"51", 52:"52"                         }
def handValueToHand(handValue):
    hand = []
    while handValue > 0:
        tempCardValue = handValue % 100
        handValue = handValue / 100
        tempCard = cardValueToCard[tempCardValue]
        hand.append(tempCard)
    return hand

def printHand(hand):
    for card in hand:
        print "[" + str(card) + "]",
    print ""
    
def cardToValue(card):
    if card.suit == 1:
        if card.rank == 2:
            return 1
        if card.rank == 3:
            return 5
        if card.rank == 4:
            return 9
        if card.rank == 5:
            return 13
        if card.rank == 6:
            return 17
        if card.rank == 7:
            return 21
        if card.rank == 8:
            return 25
        if card.rank == 9:
            return 29
        if card.rank == 10:
            return 33
        if card.rank == 11:
            return 37
        if card.rank == 12:
            return 41
        if card.rank == 13:
            return 45
        if card.rank == 14:
            return 49
    elif card.suit == 2:
        if card.rank == 2:
            return 2
        if card.rank == 3:
            return 6
        if card.rank == 4:
            return 10
        if card.rank == 5:
            return 14
        if card.rank == 6:
            return 18
        if card.rank == 7:
            return 22
        if card.rank == 8:
            return 26
        if card.rank == 9:
            return 30
        if card.rank == 10:
            return 34
        if card.rank == 11:
            return 38
        if card.rank == 12:
            return 42
        if card.rank == 13:
            return 46
        if card.rank == 14:
            return 50    
    elif card.suit == 3:
        if card.rank == 2:
            return 3
        if card.rank == 3:
            return 7
        if card.rank == 4:
            return 11
        if card.rank == 5:
            return 15
        if card.rank == 6:
            return 19
        if card.rank == 7:
            return 23
        if card.rank == 8:
            return 27
        if card.rank == 9:
            return 31
        if card.rank == 10:
            return 35
        if card.rank == 11:
            return 39
        if card.rank == 12:
            return 43
        if card.rank == 13:
            return 47
        if card.rank == 14:
            return 51 
    elif card.suit == 4:
        if card.rank == 2:
            return 4
        if card.rank == 3:
            return 8
        if card.rank == 4:
            return 12
        if card.rank == 5:
            return 16
        if card.rank == 6:
            return 20
        if card.rank == 7:
            return 24
        if card.rank == 8:
            return 28
        if card.rank == 9:
            return 32
        if card.rank == 10:
            return 36
        if card.rank == 11:
            return 40
        if card.rank == 12:
            return 44
        if card.rank == 13:
            return 48
        if card.rank == 14:
            return 52

def cardToStrValue(card):
    if card.suit == 1:
        if card.rank == 2:
            return "01"
        if card.rank == 3:
            return "05"
        if card.rank == 4:
            return "09"
        if card.rank == 5:
            return "13"
        if card.rank == 6:
            return "17"
        if card.rank == 7:
            return "21"
        if card.rank == 8:
            return "25"
        if card.rank == 9:
            return "29"
        if card.rank == 10:
            return "33"
        if card.rank == 11:
            return "37"
        if card.rank == 12:
            return "41"
        if card.rank == 13:
            return "45"
        if card.rank == 14:
            return "49"
    elif card.suit == 2:
        if card.rank == 2:
            return "02"
        if card.rank == 3:
            return "06"
        if card.rank == 4:
            return "10"
        if card.rank == 5:
            return "14"
        if card.rank == 6:
            return "18"
        if card.rank == 7:
            return "22"
        if card.rank == 8:
            return "26"
        if card.rank == 9:
            return "30"
        if card.rank == 10:
            return "34"
        if card.rank == 11:
            return "38"
        if card.rank == 12:
            return "42"
        if card.rank == 13:
            return "46"
        if card.rank == 14:
            return "50"    
    elif card.suit == 3:
        if card.rank == 2:
            return "03"
        if card.rank == 3:
            return "07"
        if card.rank == 4:
            return "11"
        if card.rank == 5:
            return "15"
        if card.rank == 6:
            return "19"
        if card.rank == 7:
            return "23"
        if card.rank == 8:
            return "27"
        if card.rank == 9:
            return "31"
        if card.rank == 10:
            return "35"
        if card.rank == 11:
            return "39"
        if card.rank == 12:
            return "43"
        if card.rank == 13:
            return "47"
        if card.rank == 14:
            return "51" 
    elif card.suit == 4:
        if card.rank == 2:
            return "04"
        if card.rank == 3:
            return "08"
        if card.rank == 4:
            return "12"
        if card.rank == 5:
            return "16"
        if card.rank == 6:
            return "20"
        if card.rank == 7:
            return "24"
        if card.rank == 8:
            return "28"
        if card.rank == 9:
            return "32"
        if card.rank == 10:
            return "36"
        if card.rank == 11:
            return "40"
        if card.rank == 12:
            return "44"
        if card.rank == 13:
            return "48"
        if card.rank == 14:
            return "52"
