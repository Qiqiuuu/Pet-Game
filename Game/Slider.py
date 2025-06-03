import pygame


class Slider:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.minVal = 0
        self.maxVal = 100
        self.currentVal = 50

        self.dragging = False
        self.isHoveringSlider = False
        self.isHoveringHandle = False

        self.fontMP = 0.
        self.handleMpX = 0.1

        self.font = pygame.font.Font("Assets/Minecraft.ttf", int(self.width * self.fontMP))

        self.rectSlider = pygame.Rect((self.x - self.width / 2), (self.y - self.height / 2), self.width, self.height)
        self.slider = pygame.image.load("Assets/slider.png").convert_alpha()
        self.slider = pygame.transform.scale(self.slider, self.rectSlider.size)
        self.sliderHigh = pygame.image.load("Assets/slider_highlighted.png").convert_alpha()
        self.sliderHigh = pygame.transform.scale(self.sliderHigh, self.rectSlider.size)
        self.sliderCurr = self.slider

        self.rectHandle = pygame.Rect(self.x + self.rectSlider.width / 2, (self.y - self.height / 2),
                                      self.width * self.handleMpX,
                                      self.height)
        self.handle = pygame.image.load("Assets/slider_handle.png").convert_alpha()
        self.handle = pygame.transform.scale(self.handle, self.rectHandle.size)
        self.handleHigh = pygame.image.load("Assets/slider_handle_highlighted.png").convert_alpha()
        self.handleHigh = pygame.transform.scale(self.handleHigh, self.rectHandle.size)
        self.handleCurr = self.handle

        proportion = (self.currentVal - self.minVal) / (self.maxVal - self.minVal)
        self.handlePos = self.rectSlider.left + proportion * (self.rectSlider.width - self.rectHandle.width)
        self.rectHandle = pygame.Rect(self.handlePos, self.y - self.height / 2,
                                      self.handle.get_width(), self.handle.get_height())

    def Draw(self, screen):
        screen.blit(self.sliderCurr, self.rectSlider)
        screen.blit(self.handleCurr, self.rectHandle)

    def HandleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rectHandle.collidepoint(event.pos):
                self.dragging = True
            else:
                self.dragging = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            self.isHoveringHandle = self.rectHandle.collidepoint(event.pos[0], event.pos[1])
            self.isHoveringSlider = self.rectSlider.collidepoint(event.pos[0], event.pos[1])

            if self.isHoveringSlider:
                self.sliderCurr = self.sliderHigh
            else:
                self.sliderCurr = self.slider

            if self.isHoveringHandle:
                self.handleCurr = self.handleHigh
            else:
                self.handleCurr = self.handle

            if self.dragging:
                self.handlePos = max(self.rectSlider.left,
                                     min(event.pos[0], self.rectSlider.right - self.rectHandle.width))
                self.rectHandle = pygame.Rect(self.handlePos, self.y - self.height / 2,
                                              self.handle.get_width(), self.handle.get_height())

                proportion = (self.handlePos - self.rectSlider.left) / (self.rectSlider.width - self.rectHandle.width)
                proportion = max(0.0, min(proportion, 1.0))
                self.currentVal = int(self.minVal + proportion * (self.maxVal - self.minVal))

    def GetValue(self):
        return self.currentVal
