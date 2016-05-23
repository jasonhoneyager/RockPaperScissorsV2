class Round:

    def __init__(self):
        self.choice = None
        
    def playerTurn(self, player1, player2):
        player1.moveChoice()
        player2.moveChoice()
        
if __name__=="__main__":
        unittest.main()