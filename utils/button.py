
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
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

        if self.text:
            # Draw outline[
            pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)
            display_text(screen,self.text, self.rect.center[0], self.rect.center[1], size=12)

    def clicked(self, pos):
        x, y = pos
        if not self.x <= x <= self.x + self.width:
            return False
        if not self.y <= y <= self.y + self.height:
            return False
        return True
