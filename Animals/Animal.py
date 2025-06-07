import random
import pygame.sprite
from Animals.Action import Action


class Animal(pygame.sprite.Sprite):
    """
    Klasa Animal reprezentuje ogólne zachowanie i właściwości zwierzaka
    w grze, takie jak głód, nuda, ruch, animacje oraz interakcje.
    Dziedziczy po `pygame.sprite.Sprite` dla łatwiejszego zarządzania w grupach sprite'ów.
        """
    def __init__(self, x: float, y: float, hungerSpeed: float, boredomSpeed: float, animations: dict,
                 startingAnimation: str, animationPet: dict):
        """
        Ładuje i przygotowuje wszystkie animacje zwierzaka, ustawia początkowe statystyki,
        i konfiguruje jego zachowanie ruchowe.

        :param x: Początkowa pozycja X (horyzontalna) środka zwierzaka.
        :type x: int
        :param y: Początkowa pozycja Y (wertykalna) środka zwierzaka.
        :type y: int
        :param hungerSpeed: Szybkość, z jaką zwierzak traci głód.
        :type hungerSpeed: float
        :param boredomSpeed: Szybkość, z jaką zwierzak traci nudę.
        :type boredomSpeed: float
        :param animations: Słownik zawierający ścieżki do klatek animacji.
                           Kluczem jest nazwa animacji (np. "idle", "eat"), wartością lista ścieżek.
        :type animations: dict
        :param startingAnimation: Klucz słownika `animations` wskazujący animację początkową.
        :type startingAnimation: str
        :param animationPet: Słownik zawierający listę nazw animacji dla różnych stanów (np. "idle", "move").
                             Używany do losowego wyboru animacji.
        :type animationPet: dict
        """

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
        self.animationSpeed = 180
        self.animationPet = animationPet
        self.animations = self.AnimationsToSurface(animations)
        self.currentAnimationKey = startingAnimation
        if self.animations and self.currentAnimationKey in self.animations:
            self.image = self.animations[self.currentAnimationKey][self.currentFrame]
            self.rect = self.image.get_rect(center=(self.x, self.y))
        self.foodFrames = len(animations["eat"])
        self.boredomFrames = len(animations["pet"])

        self.bottles = ["apple", "bigorange", "bigwater", "chocolate", "cranberry", "grape", "greentea", "lemonbig",
                        "milk",
                        "orange", "pear", "rose", "sake", "tequilla", "water", "wine"]
        self.bottle = None

        self.hearts = [("shine", 12), ("boom", 7), ("pump", 8), ("spin", 8), ("star", 12)]
        self.heart = None

        self.init = True

    def AnimationsToSurface(self, animationData: dict) -> dict:
        """
        Ładuje wszystkie grafiki animacji z podanych ścieżek do powierzchni Pygame.

        :param animationData: Słownik, gdzie kluczem jest nazwa animacji, a wartością lista ścieżek do klatek.
        :type animationData: dict

        :returns: Słownik zawierający nazwy animacji jako klucze i listy załadowanych powierzchni Pygame jako wartości.
        :rtype: dict[str, list[pygame.Surface]]
        """
        loadedAnims = {}
        for key, paths in animationData.items():
            loadedAnims[key] = [pygame.image.load(path).convert_alpha() for path in paths]
        return loadedAnims

    def Feed(self):
        """
        Rozpoczyna akcję karmienia zwierzaka.

        Ustawia animację "eat", zwiększa poziom głodu o 10 i inicjuje animację butelek/jedzenia.
        Akcja jest wykonywana tylko, jeśli zwierzak nie jest już w innej akcji.
        """
        if not self.inAction:
            self.inAction = True
            self.currentAnimationKey = "eat"
            self.currentFrame = 0
            self.lastUpdate = pygame.time.get_ticks()
            if self.food <= 100:
                self.food += 10
                self.bottle = Action(self, 3, self.y * 0.65, f"bottles_{random.choice(self.bottles)}_")
                self.bottle.Start()

    def Pet(self):
        """
        Rozpoczyna akcję głaskania zwierzaka.

        Ustawia animację "pet", zwiększa poziom nudy o 10 i inicjuje animację serc.
        Akcja jest wykonywana tylko, jeśli zwierzak nie jest już w innej akcji.
        """
        if not self.inAction:
            self.inAction = True
            self.currentAnimationKey = "pet"
            self.currentFrame = 0
            self.lastUpdate = pygame.time.get_ticks()
            if self.boredom <= 100:
                self.boredom += 10
                chosenHeart = random.choice(self.hearts)
                self.heart = Action(self, chosenHeart[1], self.y * 0.65, f"heart_{chosenHeart[0]}_")
                self.heart.Start()

    def CheckBoredomAndFood(self) -> bool:
        """
        Sprawdza, czy poziomy głodu i nudy zwierzaka są większe od zera.

        :returns: True, jeśli zarówno głód, jak i nuda są większe od 0, w przeciwnym razie False.
        :rtype: bool
        """
        return self.boredom > 0 and self.food > 0

    def ReduceBoredomAndFood(self):
        """
        Zmniejsza poziomy głodu i nudy zwierzaka w oparciu o ich szybkości spadku.
        """
        self.boredom -= self.boredomSpeed * 0.001
        self.food -= self.hungerSpeed * 0.001

    def Update(self, screen: pygame.Surface):
        """
        Aktualizuje stan zwierzaka, w tym jego ruch, animacje oraz stany głodu i nudy.

        Zarządza logiką ruchu (stanie/chodzenie), zmianą kierunku,
        aktualizacją klatek animacji oraz obsługą animacji akcji (jedzenie/głaskanie).

        :param screen: Powierzchnia Pygame, potrzebna do sprawdzenia granic ekranu dla ruchu.
        :type screen: pygame.Surface
        """
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
                self.currentAnimationKey = random.choice(self.animationPet["move"])
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
                    self.currentAnimationKey = random.choice(self.animationPet["move"])
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
        if self.bottle:
            self.bottle.Update()
        if self.heart:
            self.heart.Update()

    def Draw(self, screen: pygame.Surface, side: str, scale: float = 1.0):
        """
        Rysuje zwierzaka na ekranie.

        Skaluje aktualną klatkę animacji i opcjonalnie odwraca ją w zależności od kierunku
        (lewo/prawo). Rysuje również aktywne animacje butelek/serc.

        :param screen: Powierzchnia Pygame, na której ma zostać narysowany zwierzak.
        :type screen: pygame.Surface
        :param side: Kierunek, w którym zwierzak jest zwrócony dla celów odwrócenia grafiki ("right" lub "left").
        :type side: str
        :param scale: Współczynnik skalowania obrazu zwierzaka. Domyślnie 1.0.
        :type scale: float
        """
        scaledImage = pygame.transform.scale(self.image,
                                             (screen.get_width() * 0.25 * scale, screen.get_height() * 0.5 * scale))
        scaledRect = scaledImage.get_rect(center=self.rect.center)
        if self.currentSide == side:
            scaledImage = pygame.transform.flip(scaledImage, True, False)
        screen.blit(scaledImage, scaledRect)
        if self.bottle:
            self.bottle.Draw(screen)
        if self.heart:
            self.heart.Draw(screen)
