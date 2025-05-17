import pygame


class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 30)
        self.textColor = (255, 255, 255)
        self.isHovering = False

    def Draw(self, screen):
        pygame.draw.rect(screen, "blue", self.rect)
        textSurface = self.font.render(self.text, True, self.textColor)
        textRect = textSurface.get_rect(center=self.rect.center)
        screen.blit(textSurface, textRect)

    def HandleEvent(self, event):

        if event.type == pygame.MOUSEMOTION:
            self.isHovering = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.isHovering and event.button == 1:
                self.action()
