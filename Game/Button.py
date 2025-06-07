import os

import pygame

pygame.font.init()


class Button:
    """
    Klasa Button tworzy interaktywny przycisk tekstowy w Pygame.
    Obsługuje wyświetlanie tekstu, reaguje na najechanie kursora
    oraz kliknięcia, wywołując przypisaną akcję.
    """
    _current_dir = os.path.dirname(os.path.abspath(__file__))
    _project_root = os.path.abspath(os.path.join(_current_dir, '..'))
    _font_path = os.path.join(_project_root, "Game", "Assets", "Minecraft.ttf")

    def __init__(self, x: float, y: float, width: float, height: float, text: str, action,
                 font: pygame.font.Font = pygame.font.Font(_font_path, 30),
                 fontColor: str = (255, 255, 255)):
        """
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
                     Domyślnie "Assets/Minecraft.ttf" rozmiar 30.
        :type font: pygame.font.Font
        :param fontColor: Kolor tekstu przycisku w normalnym stanie (RGB). Domyślnie biały (255, 255, 255).
        :type fontColor: tuple
        """

        self.rect = pygame.Rect(x - width / 2, y - height / 2, width, height)
        self.defaultColor = fontColor
        self.text = text
        self.action = action
        self.font = font
        self.fontColor = fontColor
        self.isHovering = False

    def Draw(self, screen: pygame.Surface):
        """
        Rysuje tekst przycisku na ekranie.
        Tekst jest wyśrodkowany w obszarze `self.rect`.
        :param screen: Powierzchnia Pygame, na której ma zostać narysowany przycisk.
        :type screen: pygame.Surface
        """
        textSurface = self.font.render(self.text, True, self.fontColor)
        textRect = textSurface.get_rect(center=self.rect.center)
        screen.blit(textSurface, textRect)

    def HandleEvent(self, event: pygame.event.Event):
        """
        Obsługuje zdarzenia Pygame związane z interakcją użytkownika z przyciskiem.

        Zmienia kolor tekstu przycisku po najechaniu kursora oraz
        wywołuje przypisaną akcję po kliknięciu lewym przyciskiem myszy.

        :param event: Obiekt zdarzenia Pygame.
        :type event: pygame.event.Event
        """
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos) and not self.isHovering:
                self.isHovering = True
                self.fontColor = "white"
            elif not self.rect.collidepoint(event.pos) and self.isHovering:
                self.isHovering = False
                self.fontColor = self.defaultColor
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.isHovering and event.button == 1:
                self.action()
