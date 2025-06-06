from .ButtonIMG import ButtonIMG
from .Menu import Menu
import pygame
from Animals import Animal
from .Bar import Bar
from .End import End



class Game:
    """
    Główna klasa gry
    """

    def __init__(self, width:float, height:float, title:str):
        """
        :param width: Szerokość okna
        :type width: float
        :param height: Wysokość okna
        :type height: float
        :param title: Tytuł Gry
        :type title: str
        """

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption(title)
        pygame.init()
        pygame.mixer.init()

        self.clock = pygame.time.Clock()
        self.running = True
        self.menuActive = None
        self.gameActive = None
        self.endActive = False
        self.pet = None
        self.nextAction = None
        self.afterUpdateBars = False

        self.end = End(self)
        self.menu = Menu(self)

        self.deathSound = pygame.mixer.Sound("Game/Assets/Dark Souls - You Died.mp3")
        self.deathSound.set_volume(0.02)

        self.fadeAlpha = 0
        self.fadeDuration = 1500
        self.fadeStartTime = 0
        self.fading = False
        self.fadeIn = False

        self.barHeightMP = 0.12
        self.barWidthMP = 0.23
        self.barXMP = 0.01

        self.buttonXMP = 0.2
        self.buttonYMP = 0.9
        self.buttonHeightMP = 0.1
        self.buttonWidthMP = 0.2

        self.background = pygame.transform.scale(pygame.image.load("Game/Assets/Background/summer 2/Summer2.png"),
                                                 (self.width, self.height))
        self.bars = [Bar("Game/Assets/Boredom Bar/Boredom Bar_", self.width * self.barXMP, self.height * 0.02,
                         self.width * self.barWidthMP,
                         self.height * self.barHeightMP),
                     Bar("Game/Assets/Food Bar/Food Bar_", self.width * self.barXMP, self.height * 0.14,
                         self.width * self.barWidthMP,
                         self.height * self.barHeightMP)]

        self.buttons = [ButtonIMG(self.width / 2 + self.width * self.buttonXMP, self.height * self.buttonYMP,
                                  self.width * self.buttonWidthMP,
                                  self.height * self.buttonHeightMP, "Feed", lambda: self.pet.Feed(),
                                  image="Game/Assets/button.png",
                                  imageHigh="Game/Assets/button_highlighted.png"),
                        ButtonIMG(self.width / 2 - self.width * self.buttonXMP, self.height * self.buttonYMP,
                                  self.width * self.buttonWidthMP,
                                  self.height * self.buttonHeightMP, "Pet", lambda: self.pet.Pet(),
                                  image="Game/Assets/button.png",
                                  imageHigh="Game/Assets/button_highlighted.png")]

    def Events(self):
        """
        Metoda obsługująca eventy
        """
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
        """
        Metoda rysująca obiekty
        """
        if self.menuActive:
            self.menu.Draw(self.screen)
        if self.gameActive:
            self.screen.blit(self.background, (0, 0))
            if self.afterUpdateBars is True:
                for bar in self.bars:
                    bar.Draw(self.screen)
            if self.pet.init:
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
        """
        Metoda która update'uje grę
        """
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
        """
        Metoda startująca grę
        """
        self.menuActive = True
        self.gameActive = False
        while self.running:
            self.Events()
            self.Update()
            self.Draw()
            self.clock.tick(60)
        pygame.quit()

    def GameStop(self):
        """
        Stopowanie gry
        """
        self.running = False

    def SetPet(self, pet: Animal):
        """
        Ustawianie zwierzaka
        :param pet: Przyjmuje nowego zwierzaka
        :type pet: Animal
        """
        self.pet = pet
        self.ChangeScene(True, self.MenuToGame)

    def MenuToGame(self):
        """
        Zmiana sceny Menu na scenę Gra
        """
        self.menuActive = False
        self.gameActive = True
        self.ChangeScene(False)

    def GameToEnd(self):
        """
        Zmiana sceny Gra na scenę End
        """
        self.gameActive = False
        self.endActive = True
        pygame.mixer.Sound.play(self.deathSound)
        self.ChangeScene(False)

    def EndToMenu(self):
        """
        Zmiana sceny End na scenę Menu
        """
        self.endActive = False
        self.menuActive = True
        self.ChangeScene(False)

    def ChangeScene(self, fadeIn:bool, nextAction=None):
        """
        Metoda zmieniająca scenę i dodająca efekt zaciemniania
        :param fadeIn: Czy rozpoczyna się zaciemnienie
        :type fadeIn: bool
        :param nextAction: Kolejna scena
        """
        self.fading = True
        self.fadeIn = fadeIn
        self.fadeStartTime = pygame.time.get_ticks()
        self.fadeAlpha = 0 if fadeIn else 255
        self.nextAction = nextAction
