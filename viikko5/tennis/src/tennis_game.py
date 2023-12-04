class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score_text = ""

        if self.player1_score == self.player2_score:
            score_text = self.tied_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score_text = self.four_score()
        else:
            score_text = self.other_score()

        return score_text
    
    def tied_score(self):
        score_text = ""
        if self.player1_score == 0:
            score_text = "Love-All"
        elif self.player1_score == 1:
            score_text = "Fifteen-All"
        elif self.player1_score == 2:
            score_text = "Thirty-All"
        else:
            score_text = "Deuce"
        
        return score_text
    
    def four_score(self):
        score_text = ""
        point_difference = self.player1_score - self.player2_score

        if point_difference == 1:
            score_text = "Advantage player1"
        elif point_difference == -1:
            score_text = "Advantage player2"
        elif point_difference >= 2:
            score_text = "Win for player1"
        else:
            score_text = "Win for player2"
        
        return score_text
    
    def other_score(self):
        score_text = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_score
            else:
                score_text = score_text + "-"
                temp_score = self.player2_score

            if temp_score == 0:
                score_text = score_text + "Love"
            elif temp_score == 1:
                score_text = score_text + "Fifteen"
            elif temp_score == 2:
                score_text = score_text + "Thirty"
            elif temp_score == 3:
                score_text = score_text + "Forty"
        
        return score_text