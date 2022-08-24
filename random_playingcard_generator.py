#ofc i made this myself its ez
import random
from random import *

color = ["Hearts", "Clubs", "Diamonds", "Spades"]
number = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
amount = 0
while amount < 1:
    print(choice(number), "of", choice(color))
    amount += 1