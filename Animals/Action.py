import os

import pygame


class Action:
    def __init__(self, pet, numFrames, y, path):
        self.pet = pet
        self.frames = []
        self.numFrames = numFrames
        self.frameDuration = pet.animationSpeed
        self.y = y
        self.path = path
        self.currentFrameIndex = 0
        self.lastUpdate = pygame.time.get_ticks()
        self.isPlaying = False
        self.hasFinished = False

        scriptDir = os.path.dirname(os.path.abspath(__file__))
        if self.path.startswith("bottles"):
            assetsBasePath = os.path.join(scriptDir, 'Pets', 'Assets', 'Bottles')
        elif self.path.startswith("heart"):
            assetsBasePath = os.path.join(scriptDir, 'Pets', 'Assets', 'Hearts')
        for i in range(1, numFrames+1):
            imageFilename = f"{self.path}{i}.png"
            fullImagePath = os.path.join(assetsBasePath, imageFilename)
            img = pygame.image.load(fullImagePath).convert_alpha()
            img = pygame.transform.scale(img, (self.pet.rect.width*7, self.pet.rect.height*7))
            self.frames.append(img)

    def Start(self):
        self.isPlaying = True
        self.hasFinished = False
        self.currentFrameIndex = 0
        self.lastUpdate = pygame.time.get_ticks()

    def Update(self):
        if not self.isPlaying or self.hasFinished:
            return
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.frameDuration:
            self.currentFrameIndex += 1
            self.lastUpdate = currentTime

            if self.currentFrameIndex >= len(self.frames):
                self.hasFinished = True
                self.isPlaying = False
                self.currentFrameIndex = len(self.frames) - 1


    def Draw(self, screen):
        if not self.isPlaying and not self.hasFinished:
            return
        if self.hasFinished and self.currentFrameIndex == len(self.frames) - 1:
            return
        if len(self.frames) > 0 and 0 <= self.currentFrameIndex < len(self.frames):
            currentImage = self.frames[self.currentFrameIndex]
            drawX = self.pet.rect.centerx - currentImage.get_width() // 2
            drawY = self.pet.rect.top - self.y
            screen.blit(currentImage, (drawX, drawY))
