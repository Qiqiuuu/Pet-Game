import pygame


class Bar:
    """
    Klasa Bar reprezentuje dynamiczny pasek stanu, którego wygląd zmienia się
    w zależności od aktualnej wartości (np. poziom życia, głodu, nudy).
    Ładuje i przechowuje grafiki paska, skaluje je i wyświetla.
    """
    def __init__(self, path: str, x: float, y: float, width: float, height: float):
        """
        :param path: Ścieżka bazowa do plików graficznych paska.
                     Oczekuje, że pliki będą nazwane np. "bar_00.png", "bar_01.png" itd.
        :type path: str
        :param x: Pozycja X lewego górnego rogu paska.
        :type x: float
        :param y: Pozycja Y lewego górnego rogu paska.
        :type y: float
        :param width: Szerokość paska.
        :type width: float
        :param height: Wysokość paska.
        :type height: float
        """
        self.path = path
        self.currentImage = None
        self.rect = pygame.Rect(x, y, width, height)
        self.imageCache = {}

    def LoadImage(self, filename: str) -> pygame.Surface:
        """
        Ładuje obraz z podanej ścieżki lub pobiera go z pamięci podręcznej, jeśli już został załadowany.

        :param filename: Pełna ścieżka do pliku graficznego obrazu.
        :type filename: str

        :returns: Załadowana powierzchnia Pygame.
        :rtype: pygame.Surface
        """
        if filename not in self.imageCache:
            image = pygame.image.load(filename).convert_alpha()
            self.imageCache[filename] = image
        return self.imageCache[filename]

    def Update(self, currentValue: int):
        """
        Aktualizuje wyświetlany obraz paska w zależności od podanej wartości.

        Obraz zmienia się w czterech progach wartości

        :param currentValue: Aktualna wartość, na podstawie której ma zostać zmieniony obraz paska.
        :type currentValue: int
        """
        if currentValue > 75:
            self.currentImage = self.LoadImage(self.path + "00.png")
        elif 50 < currentValue <= 75:
            self.currentImage = self.LoadImage(self.path + "01.png")
        elif 25 < currentValue <= 50:
            self.currentImage = self.LoadImage(self.path + "02.png")
        elif currentValue <= 25:
            self.currentImage = self.LoadImage(self.path + "03.png")

    def Draw(self, screen: pygame.Surface):
        """
        Rysuje aktualny obraz paska na ekranie, skalując go do rozmiaru `self.rect`.

        :param screen: Powierzchnia Pygame, na której ma zostać narysowany pasek.
        :type screen: pygame.Surface
        """
        scaledImage = pygame.transform.scale(self.currentImage, (self.rect.width, self.rect.height))
        screen.blit(scaledImage, self.rect)
