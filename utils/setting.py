import pygame

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

FPS = 120

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 700

ROWS = COLS = 50

TOOLBAR_HEIGHT = SCREEN_HEIGHT - SCREEN_WIDTH

PIXEL_SIZE = SCREEN_WIDTH // COLS

BACKGROUND_COLOR = WHITE

DRAW_GIRD_LINES = True


def get_font(size):
    return pygame.font.SysFont("comicsans", size)


def display_text(text, x, y, size):
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', size)

    # creating a text surface on which text
    # will be drawn
    text_surface = my_font.render(text, True, WHITE)

    # create a rectangular object for the text
    # surface object
    text_rect = text_surface.get_rect()

    # setting position of the text
    text_rect.midtop = (x, y)

    # blit wil draw the text on screen
    return text_surface, text_rect
