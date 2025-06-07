import random

import pygame

from Animals.Animal import Animal


class Frog(Animal):
    """
    Reprezentuje zwierzę typu Frog (Żaba) w grze.

    Dziedziczy po klasie bazowej Animal i implementuje specyficzne dla Żaby
    animacje oraz zachowania, w tym losowy wybór typu żaby.
    """
    frogType = ["blue", "brown", "GameBoy_B&W", "GameBoy_Green", "green", "purple"]

    def __init__(self, x, y, hunger, boredom):
        """
        Losowo wybiera typ żaby, ładuje unikalne animacje dla wybranego typu
        i ustawia początkowe parametry, takie jak głód, nuda i pozycja.
        Definiuje również mapowanie kluczy akcji na klucze animacji.

        :param x: Początkowa pozycja X (horyzontalna) środka Żaby.
        :type x: int
        :param y: Początkowa pozycja Y (wertykalna) środka Żaby.
        :type y: int
        :param hunger: Początkowy poziom głodu Żaby (0-100).
        :type hunger: float
        :param boredom: Początkowy poziom nudy Żaby (0-100).
        :type boredom: float
        """

        self.choice = random.choice(Frog.frogType)
        path = f"Animals/Pets/Frog/Assets/frog_{self.choice}_spritesheet/frog_{self.choice}_spritesheet_"
        animationsData = self.LoadAnimations(path)
        self.currentAnimationKey = "idle1"
        super().__init__(x, y, hunger, boredom, animationsData, self.currentAnimationKey,
                         {"idle": ["idle1", "idle2"], "move": ["move"], "eat": ["eat"], "pet": ["pet"]})

    def LoadAnimations(self, path: str) -> dict:
        """
        Ładuje ścieżki do plików graficznych animacji dla Żaby.

        Metoda konstruuje ścieżki do poszczególnych klatek animacji na podstawie
        podanej ścieżki bazowej, uwzględniając różne typy animacji żaby.

        :param path: Ścieżka bazowa do sprite sheetów Żaby.
        :type path: str
        :returns: Słownik, gdzie kluczem jest nazwa animacji (np. "idle1", "move"),
                  a wartością lista ścieżek do klatek tej animacji.
        :rtype: dict
        """
        animations = {
            "idle1": [f"{path}00.png", f"{path}08.png", f"{path}08.png"],
            "idle2": [f"{path}19.png", f"{path}27.png", f"{path}27.png"],
            "move": [f"{path}02.png", f"{path}10.png", f"{path}18.png", f"{path}26.png", f"{path}28.png",
                     f"{path}20.png", f"{path}12.png", f"{path}04.png"],
            "eat": [f"{path}00.png", f"{path}03.png", f"{path}03.png",f"{path}03.png",f"{path}03.png",f"{path}08.png"],
            "pet": [f"{path}01.png", f"{path}09.png", f"{path}17.png", f"{path}25.png", f"{path}17.png",
                    f"{path}25.png", f"{path}17.png", f"{path}09.png"],
        }
        return animations

    def Feed(self):
        """
        Rozpoczyna akcję karmienia Żaby.

        Wywołuje metodę Feed klasy bazowej Animal, aby obsłużyć logikę karmienia.
        """
        super().Feed()

    def Pet(self):
        """
        Rozpoczyna akcję głaskania Żaby.

        Wywołuje metodę Pet klasy bazowej Animal, aby obsłużyć logikę głaskania.
        """
        super().Pet()

    def Update(self, screen: pygame.Surface):
        """
        Aktualizuje stan Żaby w każdej klatce gry.

        Wywołuje metodę Update klasy bazowej Animal, aby obsłużyć ruch, animacje
        i zmiany w statystykach głodu/nudy.

        :param screen: Powierzchnia Pygame, na której Żaba jest aktualizowana.
        :type screen: pygame.Surface
        """
        super().Update(screen)

    def Draw(self, screen: pygame.Surface, side: str = None, scale: float = 1.0):
        """
        Rysuje Żabę na ekranie.

        Wywołuje metodę Draw klasy bazowej Animal, aby narysować Żabę ze
        specyficznym skalowaniem i kierunkiem.

        :param screen: Powierzchnia Pygame, na której ma zostać narysowana Żaba.
        :type screen: pygame.Surface
        :param side: Kierunek, w którym Żaba jest zwrócona ("right" lub "left"),
                     przekazywany do metody bazowej dla ewentualnego odwrócenia grafiki.
        :type side: str
        :param scale: Współczynnik skalowania obrazu Żaby. Domyślnie 1.0.
                      W tej implementacji jest nadpisywany przez stałą wartość 1.0 (czyli bez skalowania).
        :type scale: float
        """
        super().Draw(screen,"right")
