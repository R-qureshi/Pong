import pygame
import pygame.font

class Scoreboard():
    """Keeps track of the score for each player."""

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 60)

        # Prepare the initial score image.
        self.prep_score()

    def prep_score(self):

        p1_score = str(self.stats.p1_score)
        p2_score = str(self.stats.p2_score)

        self.score_image = self.font.render(p1_score, True, self.text_colour, self.ai_settings.bg_colour)
        self.score2_image = self.font.render(p2_score, True, self.text_colour, self.ai_settings.bg_colour)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score2_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 150
        self.score2_rect.left = self.screen_rect.left + 150
        self.score_rect.top = 20
        self.score2_rect.top = 20


    def show_score(self):
        """Display score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.score2_image, self.score2_rect)



