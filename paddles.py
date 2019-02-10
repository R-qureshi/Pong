import pygame
from settings import *


class Paddles():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/paddle.bmp')
        self.image2 = pygame.image.load('images/paddle.bmp')

        self.paddle_1 = self.image.get_rect()
        self.paddle_2 = self.image2.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new paddle at the middle left and right of the screen
        self.paddle_1.midleft = self.screen_rect.midleft
        self.paddle_2.midright = self.screen_rect.midright

        #Movement Flags
        self.move_up = False
        self.move_down = False

        self.move_up2 = False
        self.move_down2 = False

    def move_paddle(self):
        """Update paddles position based on the movement flag."""
        if self.move_up and self.paddle_1.top > self.screen_rect.top:
            self.paddle_1.top -= 20
        if self.move_down and self.paddle_1.bottom < self.screen_rect.bottom:
            self.paddle_1.bottom += 20

        if self.move_up2 and self.paddle_2.top > self.screen_rect.top:
            self.paddle_2.top -= 20
        if self.move_down2 and self.paddle_1.bottom < self.screen_rect.bottom:
            self.paddle_2.bottom += 20


    def blitme(self):
        self.screen.blit(self.image, self.paddle_1)
        self.screen.blit(self.image2, self.paddle_2)
