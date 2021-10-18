from .setting import *


class BUTTON:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # Draw outline
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)

        if self.text:
            text_surface, text_rect = display_text(self.text, self.x, self.y, size=22)
            screen.blit(text_surface, text_rect)

    def clicked(self, pos):
        pass
