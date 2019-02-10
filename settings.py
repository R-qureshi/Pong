import pygame
import random
from pygame.locals import *
from random import randint

class Settings():
    """A class to store all settings for Ping Pong"""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_colour = (0, 0, 0)

        # Draw centre line
        self.line_colour= (255, 255, 255)
        self.central_line = pygame.Rect(self.screen_width / 2, 0, 1, self.screen_height)

        #Paddle settings
        self.paddle_speed = 0.75
        self.paddle_width = 9
        self.paddle_height = 138

        #Ball settings
        self.ball_speed = 10
        self.ball_width = 10
        self.ball_height = 10
        self.ball_dx = 10
        self.ball_dy = 10

        self.movex = random.randint(10, 10)
        self.movey = random.randint(10, 10)










