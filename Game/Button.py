import pygame

pygame.font.init()


class Button:
    def __init__(self, x, y, width, height, text, action, font=pygame.font.Font("Assets/Minecraft.ttf",30), fontColor=(255, 255, 255)):
        self.rect = pygame.Rect(x - width / 2, y - height / 2, width, height)
        self.defaultColor = fontColor
        self.text = text
        self.action = action
        self.font = font
        self.fontColor = fontColor
        self.isHovering = False

    def Draw(self, screen):
        textSurface = self.font.render(self.text, True, self.fontColor)
        textRect = textSurface.get_rect(center=self.rect.center)
        screen.blit(textSurface, textRect)

    def HandleEvent(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos) and not self.isHovering:
                self.isHovering = True
                self.fontColor = "white"
            elif not self.rect.collidepoint(event.pos) and self.isHovering:
                self.isHovering = False
                self.fontColor = self.defaultColor
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.isHovering and event.button == 1:
                self.action()
