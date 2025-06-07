import pygame

from .ButtonColor import ButtonColor


class End:
    """
    Klasa End reprezentuje ekran końca gry.
    Zarządza wyświetlaniem tytułu oraz przyciskami do ponownej próby lub wyjścia z gry.
    """
    def __init__(self, game):

        """
        :param game: Instancja głównej klasy gry, używana do dostępu do szerokości/wysokości ekranu
                     oraz metod zmiany sceny lub wyjścia z gry.
        """

        self.game = game
        self.width = game.width
        self.height = game.height

        self.fontMP = 0.12
        self.Font = pygame.font.Font("Game/Assets/OptimusPrincepsSemiBold.ttf", int(self.width * self.fontMP))
        self.endTitleSurf, self.endTitleRect = self.CreateTextRect("YOU DIED", self.Font, 0.5, 0.3)

        buttonWidth = int(self.width * 0.2)
        buttonHeight = int(self.height * 0.15)
        buttonY = int(self.height * 0.7)

        self.buttons = [
            ButtonColor(int(self.width * 0.3), buttonY, buttonWidth, buttonHeight, "Try Again", self.RestartGame,
                        font=pygame.font.Font("Game/Assets/OptimusPrincepsSemiBold.ttf", int(self.width * 0.04)),
                        fontColor="red",color="black" ),
            ButtonColor(int(self.width * 0.7), buttonY, buttonWidth, buttonHeight, "Give Up", self.ExitGame,
                        font=pygame.font.Font("Game/Assets/OptimusPrincepsSemiBold.ttf", int(self.width * 0.04)),
                        fontColor="red",
                        color="black"
                        )
        ]

    def CreateTextRect(self, text: str, font: pygame.font.Font, xPercent: float, yPercent: float):
        """
        Tworzy powierzchnię tekstową i jej prostokąt do wyświetlenia na ekranie.

        :param text: Tekst do wyrenderowania.
        :type text: str
        :param font: Obiekt czcionki Pygame do użycia.
        :type font: pygame.font.Font
        :param xPercent: Procentowa pozycja X środka tekstu na ekranie (0.0 - 1.0).
        :type xPercent: float
        :param yPercent: Procentowa pozycja Y środka tekstu na ekranie (0.0 - 1.0).
        :type yPercent: float

        :returns: Krotka zawierająca powierzchnię tekstową i jej prostokąt.
        :rtype: tuple[pygame.Surface, pygame.Rect]
        """
        surface = font.render(text, True, "red")
        rect = surface.get_rect(
            center=(int(self.width * xPercent), int(self.height * yPercent)))
        return surface, rect

    def HandleEvent(self, event: pygame.event.Event):
        """
        Obsługuje zdarzenia Pygame dla przycisków na ekranie końca gry.

        Przekazuje zdarzenia do wszystkich instancji ButtonColor.

        :param event: Obiekt zdarzenia Pygame.
        :type event: pygame.event.Event
        """
        for button in self.buttons:
            button.HandleEvent(event)

    def Draw(self, screen):
        """
        Rysuje wszystkie elementy ekranu końca gry na ekranie.

        Obejmuje tło (czarne), tytuł "YOU DIED" oraz przyciski.

        :param screen: Powierzchnia Pygame, na której ma zostać narysowany ekran końca gry.
        :type screen: pygame.Surface
        """
        screen.fill("black")
        screen.blit(self.endTitleSurf, self.endTitleRect)
        for button in self.buttons:
            button.Draw(screen)

    def ExitGame(self):
        """
        Ustawia flagę `running` głównej klasy gry na False, co prowadzi do wyjścia z aplikacji.
        """
        self.game.running = False

    def RestartGame(self):
        """
        Zmienia scenę gry na scenę menu, resetując rozgrywkę.
        """
        self.game.ChangeScene(True, self.game.EndToMenu)
