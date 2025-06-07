import random
import pygame
from Animals.Animal import Animal


class Cat(Animal):
    """
    Reprezentuje zwierzę typu Cat (Kot) w grze.

    Dziedziczy po klasie bazowej Animal i implementuje specyficzne dla Kota
    animacje oraz zachowania, w tym losowy wybór typu kota.
    """
    catType = ["hairless", "radioactive", "dark", "brown", "black", "white", "seal_point", "orange"]

    def __init__(self, x: float, y: float, hunger: float, boredom: float):
        """
        Losowo wybiera typ kota, ładuje unikalne animacje dla wybranego typu
        i ustawia początkowe parametry, takie jak głód, nuda i pozycja.

        :param x: Początkowa pozycja X (horyzontalna) środka Kota.
        :type x: float
        :param y: Początkowa pozycja Y (wertykalna) środka Kota.
        :type y: float
        :param hunger: Początkowy poziom głodu Kota (0-100).
        :type hunger: float
        :param boredom: Początkowy poziom nudy Kota (0-100).
        :type boredom: float
        """


        self.choice = random.choice(Cat.catType)
        path = f"Animals/Pets/Cat/Assets/{self.choice}/{self.choice}_"
        animationsData = self.LoadAnimations(path)
        self.currentAnimationKey = "idle"
        super().__init__(x, y, hunger, boredom, animationsData, self.currentAnimationKey,
                         {"idle": ["idle"], "move": ["run"], "eat": ["eat"], "pet": ["pet"]})

    def LoadAnimations(self, path: str) -> dict:
        """
        Ładuje ścieżki do plików graficznych animacji dla Kota.

        Metoda konstruuje ścieżki do poszczególnych klatek animacji na podstawie
        podanej ścieżki bazowej, uwzględniając różne typy animacji kota.

        :param path: Ścieżka bazowa do sprite sheetów Kota.
        :type path: str
        :returns: Słownik, gdzie kluczem jest nazwa animacji (np. "idle", "run"),
                  a wartością lista ścieżek do klatek tej animacji.
        :rtype: dict
        """
        animations = {
            "idle": [f"{path}{i}.png" for i in range(96, 100)] + [f"{path}{i}.png" for i in range(128, 130)]
                    + [f"{path}129.png"] * 20,
            "eat": [f"{path}{i}.png" for i in range(96, 100)] +
                   [f"{path}{i}.png" for i in range(128, 130)] +
                   [f"{path}{i}.png" for i in range(100, 104)] +
                   [f"{path}132.png"],
            "pet": [f"{path}{i}.png" for i in range(96, 100)] +
                   [f"{path}{i}.png" for i in range(128, 130)] +
                   [f"{path}{i}.png" for i in range(104, 108)] +
                   [f"{path}{i}.png" for i in range(136, 140)],
            "walk": [f"{path}{i}.png" for i in range(108, 112)],
            "run": [f"{path}{i}.png" for i in range(116, 120)] + [f"{path}{i}.png" for i in range(148, 152)]
        }
        return animations

    def Feed(self):
        """
        Rozpoczyna akcję karmienia Kota.

        Wywołuje metodę Feed klasy bazowej Animal, aby obsłużyć logikę karmienia.
        """
        super().Feed()

    def Pet(self):
        """
        Rozpoczyna akcję głaskania Kota.

        Wywołuje metodę Pet klasy bazowej Animal, aby obsłużyć logikę głaskania.
        """
        super().Pet()

    def Update(self, screen: pygame.Surface):
        """
        Aktualizuje stan Kota w każdej klatce gry.

        Wywołuje metodę Update klasy bazowej Animal, aby obsłużyć ruch, animacje
        i zmiany w statystykach głodu/nudy.

        :param screen: Powierzchnia Pygame, na której Kot jest aktualizowany.
        :type screen: pygame.Surface
        """
        super().Update(screen)

    def Draw(self, screen: pygame.Surface, side: str = None, scale: float = 1.0):
        """
        Rysuje Kota na ekranie.

        Wywołuje metodę Draw klasy bazowej Animal, aby narysować Kota ze
        specyficznym skalowaniem i kierunkiem.

        :param screen: Powierzchnia Pygame, na której ma zostać narysowany Kot.
        :type screen: pygame.Surface
        :param side: Kierunek, w którym Kot jest zwrócony ("right" lub "left"),
                     przekazywany do metody bazowej dla ewentualnego odwrócenia grafiki.
        :type side: str
        :param scale: Współczynnik skalowania obrazu Kota. Domyślnie 1.0.
                      W tej implementacji jest nadpisywany przez stałą wartość 0.7.
        :type scale: float
        """
        super().Draw(screen, "right", scale=0.7)
