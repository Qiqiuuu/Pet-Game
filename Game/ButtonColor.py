import pygame

from Button import Button


class ButtonColor(Button):
    def __init__(self, x, y, width, height, text, action, font, fontColor, color):
        super().__init__(x, y, width, height, text, action, font, fontColor)
        self.color = color

    def Draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        super().Draw(screen)


    def HandleEvent(self, event):
        super().HandleEvent(event)
