import random
import pygame
import pygame.mixer

from Animals.Animal import Animal

pygame.mixer.init()
class Cow(Animal):
    """
    Reprezentuje zwierzę typu Cow (Krowa) w grze.

    Dziedziczy po klasie bazowej Animal i implementuje specyficzne dla Krowy
    animacje, zachowania, a także odtwarzanie dźwięku.
    """
    cowType = ["beige", "brown", "black", "grey", "white", "white_darkspots", "white_pinkspots"]

    def __init__(self, x: int, y: int, hunger: float, boredom: float):

        """
        Losowo wybiera typ krowy, ładuje unikalne animacje dla wybranego typu.
        Inicjalizuje również dźwięk krowy i ustawia jego głośność.
        Ustawia początkowe parametry, takie jak głód, nuda i pozycja.
        Dla typu "white_darkspots" odtwarza dźwięk w pętli.

        :param x: Początkowa pozycja X (horyzontalna) środka Krowy.
        :type x: int
        :param y: Początkowa pozycja Y (wertykalna) środka Krowy.
        :type y: int
        :param hunger: Początkowy poziom głodu Krowy (0-100).
        :type hunger: float
        :param boredom: Początkowy poziom nudy Krowy (0-100).
        :type boredom: float
        """
        self.choice = random.choice(Cow.cowType)
        self.cow = pygame.mixer.Sound("Animals/Pets/Cow/Assets/krowa.mp3")
        self.cow.set_volume(0.06)
        path = f"Animals/Pets/Cow/Assets/cows_spritesheet_{self.choice}/cows_spritesheet_{self.choice}_"
        animationsData = self.LoadAnimations(path)
        self.currentAnimationKey = "idle"
        super().__init__(x, y, hunger, boredom, animationsData, self.currentAnimationKey,
                         {"idle": ["idle"], "move": ["move"], "eat": ["eat"], "pet": ["pet"]})
        if self.choice == "white_darkspots":
            self.cow.play(loops=-1)

    def LoadAnimations(self, path: str) -> dict:
        """
        Ładuje ścieżki do plików graficznych animacji dla Krowy.

        Metoda konstruuje ścieżki do poszczególnych klatek animacji na podstawie
        podanej ścieżki bazowej, uwzględniając różne typy animacji krowy.

        :param path: Ścieżka bazowa do sprite sheetów Krowy.
        :type path: str
        :returns: Słownik, gdzie kluczem jest nazwa animacji (np. "idle", "move"),
                  a wartością lista ścieżek do klatek tej animacji.
        :rtype: dict
        """
        animations = {
            "idle": [f"{path}00.png", f"{path}01.png", f"{path}02.png", f"{path}04.png", f"{path}05.png"],
            "eat": [f"{path}{i}.png" if i >= 10 else f"{path}0{i}.png" for i in range(8, 16)],
            "pet": [f"{path}{i}.png" if i >= 10 else f"{path}0{i}.png" for i in range(8, 16)],
            "move": [f"{path}{i}.png" for i in range(17, 20)]
        }
        return animations

    def CheckBoredomAndFood(self) -> bool:
        """
        Sprawdza poziom głodu i nudy Krowy.

        Jeśli zwierzę nie jest głodne ani znudzone, dźwięk krowy jest wyciszany i zatrzymywany.
        Wywołuje metodę CheckBoredomAndFood klasy bazowej Animal.

        :returns: True, jeśli krowa wymaga interakcji (jest głodna lub znudzona), False w przeciwnym razie.
        :rtype: bool
        """
        if not super().CheckBoredomAndFood():
            self.cow.fadeout(10)
            self.cow.stop()
        return super().CheckBoredomAndFood()

    def Feed(self):
        """
        Rozpoczyna akcję karmienia Krowy.

        Wywołuje metodę Feed klasy bazowej Animal, aby obsłużyć logikę karmienia.
        """
        super().Feed()

    def Pet(self):
        """
        Rozpoczyna akcję głaskania Krowy.

        Wywołuje metodę Pet klasy bazowej Animal, aby obsłużyć logikę głaskania.
        """
        super().Pet()

    def Update(self, screen: pygame.Surface):
        """
        Aktualizuje stan Krowy w każdej klatce gry.

        Wywołuje metodę Update klasy bazowej Animal, aby obsłużyć ruch, animacje
        i zmiany w statystykach głodu/nudy.

        :param screen: Powierzchnia Pygame, na której Krowa jest aktualizowana.
        :type screen: pygame.Surface
        """
        super().Update(screen)

    def Draw(self, screen: pygame.Surface, side: str = None, scale: float = 1.0):
        """
        Rysuje Krowę na ekranie.

        Wywołuje metodę Draw klasy bazowej Animal, aby narysować Krowę ze
        specyficznym skalowaniem i kierunkiem.

        :param screen: Powierzchnia Pygame, na której ma zostać narysowana Krowa.
        :type screen: pygame.Surface
        :param side: Kierunek, w którym Krowa jest zwrócona ("right" lub "left"),
                     przekazywany do metody bazowej dla ewentualnego odwrócenia grafiki.
        :type side: str
        :param scale: Współczynnik skalowania obrazu Krowy. Domyślnie 1.0.
                      W tej implementacji jest nadpisywany przez stałą wartość 0.8.
        :type scale: float
        """
        super().Draw(screen, "left", scale=0.8)
