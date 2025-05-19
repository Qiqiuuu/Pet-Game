import random

import pygame.sprite


class Animal(pygame.sprite.Sprite):
    def __init__(self, x, y, hungerSpeed, boredomSpeed, animations, startingAnimation, animationPet):
        self.innit = False
        super().__init__()
        self.boredom = 100
        self.food = 100
        self.x = x
        self.y = y
        self.hungerSpeed = hungerSpeed
        self.boredomSpeed = boredomSpeed
        self.currentSide = None
        self.inAction = False
        self.move = False
        self.moveSpeed = 2.5
        self.moveTimer = 0
        self.moveInterval = random.randint(2000, 5000)
        self.standTimer = 0
        self.standInterval = random.randint(1000, 3000)
        self.currentSide = random.choice("right,left")
        self.currentFrame = 0
        self.lastUpdate = pygame.time.get_ticks()
        self.animationSpeed = 220
        self.animationPet = animationPet
        self.animations = self.AnimationsToSurface(animations)
        self.currentAnimationKey = startingAnimation
        if self.animations and self.currentAnimationKey in self.animations:
            self.image = self.animations[self.currentAnimationKey][self.currentFrame]
            self.rect = self.image.get_rect(center=(self.x, self.y))
        self.foodFrames = len(animations["eat"])
        self.boredomFrames = len(animations["pet"])
        self.innit = True

    def AnimationsToSurface(self, animationData):
        loadedAnims = {}
        for key, paths in animationData.items():
            loadedAnims[key] = [pygame.image.load(path).convert_alpha() for path in paths]
        return loadedAnims

    def Feed(self):
        if not self.inAction:
            self.inAction = True
            self.currentAnimationKey = "eat"
            self.currentFrame = 0
            if self.food <= 100:
                self.food += 10

    def Pet(self):
        if not self.inAction:
            self.inAction = True
            self.currentAnimationKey = "pet"
            self.currentFrame = 0
            if self.boredom <= 100:
                self.boredom += 10

    def CheckBoredomAndFood(self):
        return self.boredom > 0 and self.food > 0

    def ReduceBoredomAndFood(self):
        self.boredom -= self.boredomSpeed * 0.01
        self.food -= self.hungerSpeed * 0.0005

    def Update(self, screen):
        now = pygame.time.get_ticks()
        if not self.inAction:
            if self.move:
                match self.currentSide:
                    case "right":
                        if screen.get_width() - self.x < screen.get_width() * 0.08:
                            self.currentSide = "left"
                    case "left":
                        if self.x < screen.get_width() * 0.08:
                            self.currentSide = "right"

                self.x += self.moveSpeed if self.currentSide == "right" else -self.moveSpeed
                self.currentAnimationKey = "move"
                if now - self.moveTimer >= self.moveInterval:
                    self.move = False
                    self.standTimer = now
                    self.currentAnimationKey = random.choice(self.animationPet["idle"])
                    self.currentFrame = 0
            else:
                if now - self.standTimer >= self.standInterval:
                    self.move = True
                    self.moveTimer = now
                    self.currentSide = random.choice(("left", "right"))
                    self.currentAnimationKey = "move"
                    self.currentFrame = 0
                else:
                    if now - self.lastUpdate > self.animationSpeed * 3:
                        self.lastUpdate = now
                        self.currentAnimationKey = random.choice(self.animationPet["idle"])
                        self.currentFrame = 0
        elif self.inAction:
            if self.currentAnimationKey in self.animations:
                animationFrames = self.animations[self.currentAnimationKey]
                if now - self.lastUpdate > self.animationSpeed:
                    if self.currentFrame >= len(animationFrames) - 1:
                        self.inAction = False
                        self.currentFrame = 0

        if self.currentAnimationKey in self.animations:
            if now - self.lastUpdate > self.animationSpeed:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(self.animations[self.currentAnimationKey])
                self.image = self.animations[self.currentAnimationKey][self.currentFrame]
                self.rect = self.image.get_rect(center=self.rect.center)
                self.rect.center = (self.x, self.y)
        self.rect.center = (self.x, self.y)
        self.ReduceBoredomAndFood()

    def Draw(self, screen, side, scale=1):
        scaledImage = pygame.transform.scale(self.image,
                                             (screen.get_width() * 0.25 * scale, screen.get_height() * 0.5 * scale))
        scaledRect = scaledImage.get_rect(center=self.rect.center)
        if self.currentSide == side:
            scaledImage = pygame.transform.flip(scaledImage, True, False)
        screen.blit(scaledImage, scaledRect)
