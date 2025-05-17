import pygame


class Bar:
    def __init__(self, path: str, x: int, y: int, width: int, height: int):
        self.path = path
        self.currentImage = None
        self.rect = pygame.Rect(x, y, width, height)
        self.imageCache = {}

    def LoadImage(self, filename: str) -> pygame.Surface:
        if filename not in self.imageCache:
            image = pygame.image.load(filename).convert_alpha()
            self.imageCache[filename] = image
        return self.imageCache[filename]

    def Update(self, currentValue: int):
        if currentValue > 75:
            self.currentImage = self.LoadImage(self.path + "00.png")
        elif 50 < currentValue <= 75:
            self.currentImage = self.LoadImage(self.path + "01.png")
        elif 25 < currentValue <= 50:
            self.currentImage = self.LoadImage(self.path + "02.png")
        elif currentValue <= 25:
            self.currentImage = self.LoadImage(self.path + "03.png")

    def Draw(self, screen):
        scaledImage = pygame.transform.scale(self.currentImage, (self.rect.width, self.rect.height))
        screen.blit(scaledImage, self.rect)
