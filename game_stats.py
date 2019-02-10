from settings import *

class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False

        self.high_score = 0


    def reset_stats(self):
        self.p1_score = 0
        self.p2_score = 0
