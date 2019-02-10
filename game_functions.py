import sys, pygame
from settings import *


def update_screen(ai_settings, screen, stats, sb, paddles, ball):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_colour)
    paddles.blitme()
    ball.blitme()
    sb.show_score()
    ball.paddle_collision(paddles)
    clock = pygame.time.Clock()
    ai_settings.central_line
    pygame.draw.rect(screen, ai_settings.line_colour, ai_settings.central_line)
    pygame.display.update()
    clock.tick(30)


def check_keydown_events(event, paddles, paddle_2):
    """Respond to keypresses."""
    if event.key == pygame.K_w:
        paddles.move_up = True
    elif event.key == pygame.K_s:
        paddles.move_down = True

    if event.key == pygame.K_UP:
        paddles.move_up2 = True
    elif event.key == pygame.K_DOWN:
        paddles.move_down2 = True


def check_keyup_events(event, paddles, paddle_2):
    """Respond to key releases."""
    if event.key == pygame.K_w:
        paddles.move_up = False
    elif event.key == pygame.K_s:
        paddles.move_down = False

    if event.key == pygame.K_UP:
        paddles.move_up2 = False
    elif event.key == pygame.K_DOWN:
        paddles.move_down2 = False

def check_events(paddles, paddle_2):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddles, paddle_2)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddles, paddle_2)



