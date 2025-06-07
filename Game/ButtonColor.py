import pygame

from .Button import Button


class ButtonColor(Button):
    """
    Klasa ButtonColor rozszerza funkcjonalność klasy Button, dodając możliwość
    rysowania prostokątnego tła przycisku w określonym kolorze.
    """
    def __init__(self, x: float, y: float, width: float, height: float, text: str, action,
                 font: pygame.font.Font, fontColor: str, color: str):
        """
         Dziedziczy wszystkie parametry i zachowania z klasy `Button`,
        dodając możliwość określenia koloru tła przycisku.

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
        :param font: Obiekt czcionki Pygame do użycia dla tekstu przycisku.
        :type font: pygame.font.Font
        :param fontColor: Kolor tekstu przycisku w normalnym stanie (RGB).
        :type fontColor: tuple
        :param color: Kolor tła prostokąta przycisku (RGB).
        :type color: tuple
        """
        super().__init__(x, y, width, height, text, action, font, fontColor)
        self.color = color

    def Draw(self, screen: pygame.Surface):
        """
        Rysuje prostokątne tło przycisku, a następnie tekst na nim.

        Wywołuje metodę `Draw` z klasy nadrzędnej (Button) do rysowania tekstu.

        :param screen: Powierzchnia Pygame, na której ma zostać narysowany przycisk.
        :type screen: pygame.Surface
        """
        pygame.draw.rect(screen, self.color, self.rect)
        super().Draw(screen)


    def HandleEvent(self, event: pygame.event.Event):
        """
        Obsługuje zdarzenia Pygame dla przycisku.

        Przekazuje zdarzenia do metody `HandleEvent` z klasy nadrzędnej (Button).
        To obsłuży zmianę koloru tekstu przy najechaniu i wywołanie akcji przy kliknięciu.

        :param event: Obiekt zdarzenia Pygame.
        :type event: pygame.event.Event
        """
        super().HandleEvent(event)
