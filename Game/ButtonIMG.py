import pygame

from Button import Button


class ButtonIMG(Button):
    def __init__(self, x, y, width, height, text, action, image, imageHigh):
        super().__init__(x, y, width, height, text, action, pygame.font.Font("Assets/Minecraft.ttf",int(width*0.15)), (255, 255, 255))
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.rect.size)
        self.imageHigh = pygame.image.load(imageHigh).convert_alpha()
        self.imageHigh = pygame.transform.scale(self.imageHigh, self.rect.size)
        self.imageCurr = self.image

    def Draw(self, screen):
        screen.blit(self.imageCurr, self.rect)
        super().Draw(screen)

    def HandleEvent(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos) and not self.isHovering:
                self.isHovering = True
                self.fontColor = "white"
                self.imageCurr = self.imageHigh
            elif not self.rect.collidepoint(event.pos) and self.isHovering:
                self.isHovering = False
                self.fontColor = self.defaultColor
                self.imageCurr = self.image
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.isHovering and event.button == 1:
                self.action()
