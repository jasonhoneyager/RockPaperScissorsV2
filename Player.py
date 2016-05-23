class Player:

    def __init__(self):
        self.name = None
        self.move = None
        self.hand = None
        
    def obtainName(self):
        NAME = input("Please enter your name: ")
        self.name = NAME
        
    def moveChoice(self):
        Turn = True
        while Turn:
            print("Choose your Hand")
            Hand = input("Rock, Paper, Scissors, Lizard, Spock: ")
            if Hand == "Rock":
                Value = 0
                Turn = False
            elif Hand == "Spock":
                Value = 1
                Turn = False
            elif Hand == "Paper":
                Value = 2
                Turn = False
            elif Hand == "Lizard":
                Value = 3
                Turn = False
            elif Hand == "Scissors":
                Value = 4
                Turn = False
            else: print("Please choose a hand:")
        print(self.name,"chose",Hand)    
        self.move = Value
        self.hand = Hand
            
if __name__=="__main__":
        unittest.main()