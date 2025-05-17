import pygame


class Slider:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect((self.x-self.width/2), (self.y-self.height/2), self.width, self.height)
        self.minVal = 0
        self.maxVal = 100
        self.currentVal = 50
        self.handlePos = self.x + self.width / 2
        self.dragging = False
        self.font = pygame.font.Font(None, 24)

    def Draw(self, screen):
        pygame.draw.rect(screen, "red", self.rect)
        pygame.draw.circle(screen, "pink", (self.handlePos, self.rect.centery), self.rect.height // 5)

    def HandleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.handlePos = max(self.rect.left, min(event.pos[0], self.rect.right))

    def GetValue(self):
        proportion = (self.handlePos - self.rect.left) / self.rect.width
        value = self.minVal + proportion * (self.maxVal - self.minVal)
        return int(value)
