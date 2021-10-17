import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    while True:
        for event in pygame.event.get():

            pygame.display.update()


if __name__ == "__main__":
    main()
