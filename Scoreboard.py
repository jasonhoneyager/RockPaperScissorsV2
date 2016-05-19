class Scoreboard:

    def __init__(self):
        self.score = [0, 0, 0]
        
    def updateScore(self, roundScore):
        self.score[roundScore] += 1
        print(self.score)