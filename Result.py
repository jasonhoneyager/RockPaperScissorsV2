class Result:

    def __init__(self):
        self.score = None
        
    def declareVictor(self, player1, player2):
        determineOutcome = (player1.move - player2.move) % 5
        if determineOutcome == 0:
            print("Stalemate!")
            self.score = 2
        elif determineOutcome <= 2:
            print(player1.name,"wins!",player1.hand,"beats",player2.hand)
            self.score = 0
        else:
            print(player2.name,"wins!",player2.hand,"beats",player1.hand)
            self.score = 1