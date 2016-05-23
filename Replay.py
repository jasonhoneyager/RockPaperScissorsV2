class Replay:

    def __init__(self):
        self.playAgain = True
        
    def replayGame(self):
        replay = input("Play Again? Y/N: ")
        replay = replay.lower()
        if replay in ("n","no"):
            self.playAgain = False
            
if __name__=="__main__":
        unittest.main()