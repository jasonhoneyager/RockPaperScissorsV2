import unittest
import sys
import mock

# from Game import Game
from Player import Player
# from AI import AI
from Scoreboard import Scoreboard
# from Round import Round
from Result import Result
# from Replay import Replay


class UnitTest(unittest.TestCase):
   
        # game = Game()
        # player = Player()
        # ai = AI()
        # scoreboard = Scoreboard()
        # round = Round()
        # result = Result()
        # replay = Replay()

#Game Tests########################################################################################

#Player Tests######################################################################################

#AI Tests##########################################################################################
    
#Scoreboard tests##################################################################################
    def test_updateScore_win(self):
        scoreboard = Scoreboard()
        value = 0
        scoreboard.updateScore(value)
        self.assertEqual(scoreboard.score, [1, 0, 0])
        
    def test_updateScore_lose(self):
        scoreboard = Scoreboard()
        value = 1
        scoreboard.updateScore(value)
        self.assertEqual(scoreboard.score, [0, 1, 0])
        
    def test_updateScore_tie(self):
        scoreboard = Scoreboard()
        value = 2
        scoreboard.updateScore(value)
        self.assertEqual(scoreboard.score, [0, 0, 1])
#Round Tests#######################################################################################

#Result Tests######################################################################################
    def test_declareVictor_win(self):
        result = Result()
        value1 = Player()
        value2 = Player()
        value1.name = "player1"
        value1.move = 0
        value1.hand = "Rock"
        value2.name = "player2"
        value2.move = 2
        value2.hand = "Paper"
        result.declareVictor(value1, value2)
        self.assertEqual(result.score, 0)
    def test_declareVictor_lose(sel):
        result = Result()
        value1 = Player()
        value2 = Player()
        value1.name = "player1"
        value1.move = 2
        value1.hand = "Paper"
        value2.name = "player2"
        value2.move = 0
        value2.hand = "Rock"
        result.declareVictor(value1, value2)
        self.assertEqual(result.score, 1)
    def test_declareVictor_tie(self):
        result = Result()
        value1 = Player()
        value2 = Player()
        value1.name = "player1"
        value1.move = 0
        value1.hand = "Rock"
        value2.name = "player2"
        value2.move = 0
        value2.hand = "Rock"
        result.declareVictor(value1, value2)
        self.assertEqual(result.score, 2)
#Replay Tests######################################################################################
  
        
def main():
    unittest.main()
    

        
if __name__== "__main__":
        main()
            
        # arrange
        # act
        # assert