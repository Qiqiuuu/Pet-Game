import pygame

pygame.font.init()


class Button:
    def __init__(self, x, y, width, height, text, action, font=pygame.font.Font("Assets/Minecraft.ttf",30), fontColor=(255, 255, 255),
                 image=None, imageHigh = None, color="black"):
        self.rect = pygame.Rect(x - width / 2, y - height / 2, width, height)
        self.defaultColor = fontColor
        self.text = text
        self.action = action
        self.font = font
        self.textColor = fontColor
        self.isHovering = False
        self.image = None
        if image and imageHigh is not None:
            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, self.rect.size)
            self.imageHigh = pygame.image.load(imageHigh).convert_alpha()
            self.imageHigh = pygame.transform.scale(self.imageHigh, self.rect.size)
            self.imageCurr = self.image
        self.color = color

    def Draw(self, screen):
        if self.image is not None:
            screen.blit(self.imageCurr, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        textSurface = self.font.render(self.text, True, self.textColor)
        textRect = textSurface.get_rect(center=self.rect.center)
        screen.blit(textSurface, textRect)

    def HandleEvent(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos) and not self.isHovering:
                self.isHovering = True
                self.textColor = "white"
                self.imageCurr = self.imageHigh
            elif not self.rect.collidepoint(event.pos) and self.isHovering:
                self.isHovering = False
                self.textColor = self.defaultColor
                self.imageCurr = self.image
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.isHovering and event.button == 1:
                self.action()
