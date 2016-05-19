from Player import Player
from AI import AI
from Scoreboard import Scoreboard
from Round import Round
from Result import Result
from Replay import Replay

class Game:

    def __init__(self):
        
        self.player1 = None
        self.player2 = None
        self.replayGame = None
    
    def getPlayers(self):
        while self.player2 == None:
            gameType = self.getGameType()
            if gameType == "1":
                self.player1 = self.getHumanPlayer()
                self.player2 = self.getAIPlayer()
            elif gameType == "2":
                self.player1 = self.getHumanPlayer()
                self.player2 = self.getHumanPlayer()
            else:
                print("Please Enter a Valid Value: ")
                     
    def getGameType(self):
        choice = input("Would you like to play a (1) or (2) player game? ")
        return choice
        
    def getHumanPlayer(self):
        playerData = Player()
        playerData.obtainName()
        return playerData
   
    def getAIPlayer(self):
        AIData = AI()
        return AIData
        
    def start(self):
        self.getPlayers()
        # print(self.player1.name)
        # print(self.player2.name)
        scoreboard = Scoreboard()
        while self.replayGame != False:
            round = Round()
            round.playerTurn(self.player1, self.player2)
            # print(self.player1.move, self.player2.move)
            result = Result()
            result.declareVictor(self.player1, self.player2)
            roundScore = result.score
            scoreboard.updateScore(roundScore)
            replay = Replay()
            replay.replayGame()
            self.replayGame = replay.playAgain
                     
                        
#########################################################################################################

