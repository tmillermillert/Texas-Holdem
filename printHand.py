#from TexasHoldemInclude import card
from TexasHoldemInclude import handValueToHand
from TexasHoldemInclude import printHand
import sys


printHand(handValueToHand(int(sys.argv[1])))
