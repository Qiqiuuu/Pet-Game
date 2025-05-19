import pygame


class Slider:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rectSlider = pygame.Rect((self.x-self.width/2), (self.y-self.height/2), self.width, self.height)
        self.rectHandle = pygame.Rect((self.x-self.width/2), (self.y-self.height/2), self.width*0.4, self.height*0.4)
        self.minVal = 0
        self.maxVal = 100
        self.currentVal = 50
        self.handlePos = self.x + self.width / 2
        self.dragging = False
        self.isHovering = False
        self.font = pygame.font.Font("Assets/Minecraft.ttf", int(self.width * 0.02))
        self.slider = pygame.image.load("Assets/slider.png").convert_alpha()
        self.slider = pygame.transform.scale(self.slider, self.rectSlider.size)
        self.sliderHigh = pygame.image.load("Assets/slider_highlighted.png").convert_alpha()
        self.sliderHigh = pygame.transform.scale(self.sliderHigh, self.rectSlider.size)
        self.sliderCurr = self.slider
        self.handle = pygame.image.load("Assets/slider_handle.png").convert_alpha()
        self.handle = pygame.transform.scale(self.handle, self.rectSlider.size)
        self.handleHigh = pygame.image.load("Assets/slider_handle_highlighted.png").convert_alpha()
        self.handleHigh = pygame.transform.scale(self.sliderHigh, self.rectSlider.size)
        self.handleCurr = self.handle

    def Draw(self, screen):
        screen.blit(self.sliderCurr, self.rectSlider)
        screen.blit(self.handle, self.rectHandle)

    def HandleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rectSlider.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.handlePos = max(self.rectHandle.left, min(event.pos[0], self.rectHandle.right))

    def GetValue(self):
        proportion = (self.handlePos - self.rectHandle.left) / self.rectHandle.width
        value = self.minVal + proportion * (self.maxVal - self.minVal)
        return int(value)
