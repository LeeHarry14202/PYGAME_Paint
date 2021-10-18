import pygame.mouse

from utils import *

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drawing Program")


def init_grid(rows, cols, color):
    gird_ = np.empty((rows, cols), dtype=tuple)
    gird_.fill(color)
    return gird_


def draw_gird(screen, gird_):
    for i, row in enumerate(gird_):
        for j, pixel in enumerate(row):
            pygame.draw.rect(screen, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GIRD_LINES:
        # Add 1 to draw the last row
        for i in range(ROWS + 1):
            pygame.draw.line(screen, BLACK, start_pos=(0, i * PIXEL_SIZE),
                             end_pos=(SCREEN_WIDTH, i * PIXEL_SIZE))
        # Add 1 to draw the last col
        for j in range(COLS + 1):
            pygame.draw.line(screen, BLACK, start_pos=(j * PIXEL_SIZE, 0),
                             end_pos=(j * PIXEL_SIZE, SCREEN_HEIGHT - abs(SCREEN_HEIGHT - SCREEN_WIDTH)))


def draw(screen):
    screen.fill(BACKGROUND_COLOR)
    draw_gird(screen, gird)
    button.draw(screen)
    pygame.display.update()


def get_rol_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE
    if row >= ROWS:
        raise IndexError
    return row, col


run = True
clock = pygame.time.Clock()
gird = init_grid(ROWS, COLS, BACKGROUND_COLOR)
drawing_color = BLACK
button = BUTTON(10, 600, 50, 50, BLUE, "Button")


def main():
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            left_mouse = 0
            if pygame.mouse.get_pressed()[left_mouse]:
                pos = pygame.mouse.get_pos()
                try:
                    row, col = get_rol_col_from_pos(pos)
                    gird[row, col] = drawing_color
                except IndexError:
                    pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    gird.fill(WHITE)

        draw(SCREEN)

        clock.tick(FPS)


if __name__ == "__main__":
    main()
