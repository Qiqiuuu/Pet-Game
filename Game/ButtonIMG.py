import pygame

from .Button import Button


class ButtonIMG(Button):
    """
    Klasa ButtonIMG rozszerza funkcjonalność klasy Button, dodając możliwość
    wyświetlania graficznego tła przycisku, które zmienia się po najechaniu kursorem.
    """
    def __init__(self, x: float, y: float, width: float, height: float, text: str, action,
                 image: str, imageHigh: str):
        """
        Dziedziczy podstawowe parametry i zachowania z klasy `Button`,
        dodając ścieżki do grafik przycisku w stanie normalnym i podświetlonym.

        :param x: Pozycja X środka przycisku.
        :type x: float
        :param y: Pozycja Y środka przycisku.
        :type y: float
        :param width: Szerokość przycisku.
        :type width: float
        :param height: Wysokość przycisku.
        :type height: float
        :param text: Tekst wyświetlany na przycisku.
        :type text: str
        :param action: Funkcja (callback) do wywołania po kliknięciu przycisku.
        :type action: callable
        :param image: Ścieżka do pliku graficznego dla przycisku w stanie normalnym.
        :type image: str
        :param imageHigh: Ścieżka do pliku graficznego dla przycisku w stanie podświetlonym (po najechaniu).
        :type imageHigh: str
        """
        super().__init__(x, y, width, height, text, action, pygame.font.Font("Game/Assets/Minecraft.ttf",int(width*0.15)), (255, 255, 255))
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.rect.size)
        self.imageHigh = pygame.image.load(imageHigh).convert_alpha()
        self.imageHigh = pygame.transform.scale(self.imageHigh, self.rect.size)
        self.imageCurr = self.image

    def Draw(self, screen: pygame.Surface):
        """
        Rysuje graficzne tło przycisku, a następnie tekst na nim.

        Najpierw rysuje grafikę tła , a następnie
        wywołuje metodę ``Draw`` z klasy nadrzędnej (``Button``) do rysowania tekstu.

        :param screen: Powierzchnia Pygame, na której ma zostać narysowany przycisk.
        :type screen: pygame.Surface
        """
        screen.blit(self.imageCurr, self.rect)
        super().Draw(screen)

    def HandleEvent(self, event: pygame.event.Event):
        """
        Obsługuje zdarzenia Pygame związane z interakcją użytkownika z przyciskiem graficznym.

        Metoda ta nadpisuje zachowanie z klasy nadrzędnej `Button`.
        Zmienia grafikę przycisku i kolor tekstu po najechaniu kursora myszy
        oraz wywołuje przypisaną akcję po kliknięciu lewym przyciskiem myszy.

        :param event: Obiekt zdarzenia Pygame.
        :type event: pygame.event.Event
        """
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos) and not self.isHovering:
                self.isHovering = True
                self.fontColor = "white"
                self.imageCurr = self.imageHigh
            elif not self.rect.collidepoint(event.pos) and self.isHovering:
                self.isHovering = False
                self.fontColor = self.defaultColor
                self.imageCurr = self.image
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.isHovering and event.button == 1:
                self.action()
