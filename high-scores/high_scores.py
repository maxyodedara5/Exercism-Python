"""List methods refresher"""

class HighScores:
    """Class for displaying highscores"""
    def __init__(self, scores_l):
        self.scores = scores_l

    def latest(self):
        """Last score"""
        return self.scores[-1]

    def personal_best(self):
        """Max score"""
        return max(self.scores)

    def personal_top_three(self):
        """Top three scores"""
        return sorted(self.scores, reverse=True)[:3]
