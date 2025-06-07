import pygame

from Animals.Animal import Animal


class BlobFish(Animal):
    """
        Reprezentuje zwierzę typu BlobFish w grze.

        Dziedziczy po klasie bazowej Animal i implementuje specyficzne dla BlobFisha animacje
        oraz zachowania.
        """

    def __init__(self, x: float, y: float, hunger: float, boredom: float):
        """
        Ładuje unikalne animacje dla BlobFisha i ustawia początkowe parametry,
        takie jak głód, nuda i pozycja.

        :param x: Początkowa pozycja X (horyzontalna) środka BlobFisha.
        :type x: float
        :param y: Początkowa pozycja Y (wertykalna) środka BlobFisha.
        :type y: float
        :param hunger: Początkowy poziom głodu BlobFisha (0-100).
        :type hunger: float
        :param boredom: Początkowy poziom nudy BlobFisha (0-100).
        :type boredom: float
        """

        path = f"Animals/Pets/BlobFish/Assets/Blobfish Spritesheet_"
        animationsData = self.LoadAnimations(path)
        self.currentAnimationKey = "idle"
        super().__init__(x, y, hunger, boredom, animationsData, self.currentAnimationKey,
                         {"idle": ["idle"], "move": ["move"], "eat": ["eat"], "pet": ["pet"]})

    def LoadAnimations(self, path: str) -> dict:
        """
        Ładuje ścieżki do plików graficznych animacji dla BlobFisha.

        Metoda konstruuje ścieżki do poszczególnych klatek animacji na podstawie
        podanej ścieżki bazowej.

        :param path: Ścieżka bazowa do sprite sheetów BlobFisha.
        :type path: str
        :returns: Słownik, gdzie kluczem jest nazwa animacji (np. "idle", "eat"),
                  a wartością lista ścieżek do klatek tej animacji.
        :rtype: dict
        """
        animations = {
            "idle": [f"{path}01.png"],
            "eat": [f"{path}{i}.png" for i in range(12, 17)] + [f"{path}{i}.png" for i in range(16, 11, -1)],
            "pet": [f"{path}{i}.png" for i in range(19, 23)] + [f"{path}{i}.png" for i in range(22, 18, -1)],
            "move": [f"{path}{i}.png" if i >= 10 else f"{path}0{i}.png" for i in range(1, 12)]
        }
        return animations

    def Feed(self):
        """
        Rozpoczyna akcję karmienia BlobFisha.

        Wywołuje metodę Feed klasy bazowej Animal, aby obsłużyć logikę karmienia.
        """
        super().Feed()

    def Pet(self):
        """
        Rozpoczyna akcję głaskania BlobFisha.

        Wywołuje metodę Pet klasy bazowej Animal, aby obsłużyć logikę głaskania.
        """
        super().Pet()

    def Update(self, screen: pygame.Surface):
        """
        Aktualizuje stan BlobFisha w każdej klatce gry.

        Wywołuje metodę Update klasy bazowej Animal, aby obsłużyć ruch, animacje
        i zmiany w statystykach głodu/nudy.

        :param screen: Powierzchnia Pygame, na której BlobFish jest aktualizowany.
        :type screen: pygame.Surface
        """
        super().Update(screen)

    def Draw(self, screen: pygame.Surface, side: str = None, scale: float = 1.0):
        """
        Rysuje BlobFisha na ekranie.

        Wywołuje metodę Draw klasy bazowej Animal, aby narysować BlobFisha ze
        specyficznym skalowaniem i kierunkiem.

        :param screen: Powierzchnia Pygame, na której ma zostać narysowany BlobFish.
        :type screen: pygame.Surface
        :param side: Kierunek, w którym Kot jest zwrócony ("right" lub "left"),
                     przekazywany do metody bazowej dla ewentualnego odwrócenia grafiki.
        :type side: str
        :param scale: Współczynnik skalowania obrazu BlobFish. Domyślnie 1.0.
                      W tej implementacji jest nadpisywany przez stałą wartość 0.7.
        :type scale: float
        """
        super().Draw(screen, "right", scale=0.6)
