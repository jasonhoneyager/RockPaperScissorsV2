import os
import random

class AI:

    def __init__(self):
        self.name = "CPU Player"
        self.move = None
        self.hand = None
        
    def moveChoice(self):
        moveChoice = random.randrange(0,4)
        if moveChoice == 0: Hand = "Rock"
        elif moveChoice == 1: Hand = "Spock"
        elif moveChoice == 2: Hand = "Paper"
        elif moveChoice == 3: Hand = "Lizard"
        elif moveChoice == 4: Hand = "Scissors"
        print(self.name,"chose",Hand)
        self.move = moveChoice
        self.hand = Hand