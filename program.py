import pygame, random

from settings import Settings
from paddles import *
from ball import Ball
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():
    # Initialise pygame, settings and screen object.
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    paddles = Paddles(ai_settings, screen)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ball = Ball(ai_settings, screen, paddles)


    # Start the main loop for the game.
    while True:
        gf.check_events(paddles, paddles.paddle_2)
        paddles.move_paddle()
        ball.move_ball()
        ball.wall_collision(stats, sb)
        gf.update_screen(ai_settings, screen, stats, sb, paddles, ball)


run_game()
