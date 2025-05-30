from Menu import Menu
import pygame
from Animals import Animal
from Bar import Bar
from Button import Button
from End import End


class Game:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.background = pygame.transform.scale(pygame.image.load("Assets/Background/summer 2/Summer2.png"),
                                                 (self.width, self.height))
        self.bars = [Bar("Assets/Boredom Bar/Boredom Bar_", self.width * 0.01, self.height * 0.02, self.width * 0.23,
                         self.height * 0.12),
                     Bar("Assets/Food Bar/Food Bar_", self.width * 0.01, self.height * 0.14, self.width * 0.23,
                         self.height * 0.12)]

        self.menuActive = None
        self.gameActive = None
        self.menu = Menu(self)
        self.pet = None
        self.fadeAlpha = 0
        self.fading = False
        self.fadeIn = False
        self.fadeDuration = 1500
        self.fadeStartTime = 0
        self.nextAction = None
        self.afterUpdateBars = False
        self.buttons = [Button(self.width / 2 + self.width * 0.2, self.height * 0.9, self.width * 0.2,
                               self.height * 0.1, "Feed", lambda: self.pet.Feed(),
                               image="Assets/button.png",
                               imageHigh="Assets/button_highlighted.png"),
                        Button(self.width / 2 - self.width * 0.2, self.height * 0.9, self.width * 0.2,
                               self.height * 0.1, "Pet", lambda: self.pet.Pet(),
                               image="Assets/button.png",
                               imageHigh="Assets/button_highlighted.png")]
        self.endActive = False
        self.end = End(self)
        self.deathSound = pygame.mixer.Sound("Assets/Dark Souls - You Died.mp3")
        self.deathSound.set_volume(0.02)

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            for button in self.buttons:
                button.HandleEvent(event)
            if self.menuActive:
                self.menu.HandleEvent(event)
            if self.endActive:
                self.end.HandleEvent(event)

    def Draw(self):
        if self.menuActive:
            self.menu.Draw(self.screen)
        if self.gameActive:
            self.screen.blit(self.background, (0, 0))
            if self.afterUpdateBars is True:
                for bar in self.bars:
                    bar.Draw(self.screen)
            if self.pet.innit:
                self.pet.Draw(self.screen)
            for button in self.buttons:
                button.Draw(self.screen)
        if self.endActive:
            self.end.Draw(self.screen)
        if self.fading:
            fadeSurface = pygame.Surface((self.width, self.height))
            fadeSurface.fill((0, 0, 0))
            fadeSurface.set_alpha(self.fadeAlpha)
            self.screen.blit(fadeSurface, (0, 0))
        pygame.display.flip()

    def Update(self):
        if self.gameActive and not self.pet.CheckBoredomAndFood() and not self.fading:
            self.ChangeScene(True, self.GameToEnd)
        if self.menuActive:
            self.menu.Update()
        if self.gameActive:
            for bar, value in zip(self.bars, [self.pet.boredom, self.pet.food]):
                bar.Update(value)
            self.afterUpdateBars = True
            self.pet.Update(self.screen)
        if self.fading:
            currentTime = pygame.time.get_ticks()
            elapsedTime = currentTime - self.fadeStartTime
            if elapsedTime >= self.fadeDuration:
                self.fading = False
                self.fadeAlpha = 255 if self.fadeIn else 0
                if self.nextAction:
                    self.nextAction()
                    self.nextAction = None
            else:
                if self.fadeIn:
                    self.fadeAlpha = int(255 * (elapsedTime / self.fadeDuration))
                else:
                    self.fadeAlpha = int(255 * (1 - (elapsedTime / self.fadeDuration)))

    def GameStart(self):
        self.menuActive = True
        self.gameActive = False
        while self.running:
            self.Events()
            self.Update()
            self.Draw()
            self.clock.tick(60)
        pygame.quit()

    def GameStop(self):
        self.running = False

    def SetPet(self, pet: Animal):
        self.pet = pet
        self.ChangeScene(True, self.MenuToGame)

    def MenuToGame(self):
        self.menuActive = False
        self.gameActive = True
        self.ChangeScene(False)

    def GameToEnd(self):
        self.gameActive = False
        self.endActive = True
        pygame.mixer.Sound.play(self.deathSound)
        self.ChangeScene(False)

    def EndToMenu(self):
        self.endActive = False
        self.menuActive = True
        self.ChangeScene(False)

    def ChangeScene(self, fadeIn, nextAction=None):
        self.fading = True
        self.fadeIn = fadeIn
        self.fadeStartTime = pygame.time.get_ticks()
        self.fadeAlpha = 0 if fadeIn else 255
        self.nextAction = nextAction


if __name__ == "__main__":
    gra = Game(1920, 1080, "Pet Game")
    gra.GameStart()
