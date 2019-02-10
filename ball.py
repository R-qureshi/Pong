import pygame, random, sys
from pygame.sprite import Sprite


class Ball(Sprite):
    """class represents the ball that bounces around."""

    # Constructor function
    def __init__(self, ai_settings, screen, paddles):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.paddles = paddles

        # Load the ball image and set its rect attribute
        self.image = pygame.image.load('images/ball.bmp')
        self.ball = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ball.center = self.screen_rect.center


        # Score settings
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 60)


    def move_ball(self):
        self.ball.x += self.ai_settings.movex
        self.ball.y += self.ai_settings.movey


    def wall_collision(self, stats, sb):
        """Check if ball collides with the walls."""
        if self.ball.x < 0:
            self.ai_settings.movex *= -1
            stats.p1_score += 1
            sb.prep_score()

        if self.ball.x > self.screen_rect.right - self.ai_settings.ball_width:
            self.ai_settings.movex *= -1
            stats.p2_score += 1
            sb.prep_score()


        if self.ball.y < 0 or self.ball.y > self.screen_rect.bottom - self.ai_settings.ball_height:
            self.ai_settings.movey *= -1


    def paddle_collision(self, paddles):
        """If ball collides with paddles increase speed by 2"""
        if self.ball.colliderect(paddles.paddle_1):
            self.ai_settings.movex *= -1
            self.ai_settings.movex += 2
            self.ai_settings.movey += 2

        if self.ball.colliderect(paddles.paddle_2):
            self.ai_settings.movex *= -1
            self.ai_settings.movex += 2
            self.ai_settings.movey += 2

    def blitme(self):
        self.screen.blit(self.image, self.ball)


