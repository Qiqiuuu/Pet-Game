import pygame
from Button import Button


class End:
    def __init__(self, game):
        self.game = game
        self.width = game.width
        self.height = game.height
        self.Font = pygame.font.Font("Assets/OptimusPrincepsSemiBold.ttf", int(self.width * 0.12))
        self.endTitleSurf, self.endTitleRect = self.CreateTextRect("YOU DIED", self.Font, 0.5, 0.3)

        buttonWidth = int(self.width * 0.2)
        buttonHeight = int(self.height * 0.15)
        buttonY = int(self.height * 0.7)

        self.buttons = [
            Button(int(self.width * 0.3), buttonY, buttonWidth, buttonHeight, "Try Again", self.RestartGame,
                   font=pygame.font.Font("Assets/OptimusPrincepsSemiBold.ttf", int(self.width * 0.04)),
                   fontColor="red",),
            Button(int(self.width * 0.7), buttonY, buttonWidth, buttonHeight, "Give Up", self.ExitGame,
                   font=pygame.font.Font("Assets/OptimusPrincepsSemiBold.ttf", int(self.width * 0.04)),
                   fontColor="red",
                   )
        ]

    def CreateTextRect(self, text, font, xPercent, yPercent):
        surface = font.render(text, True, "red")
        rect = surface.get_rect(
            center=(int(self.width * xPercent), int(self.height * yPercent)))
        return surface, rect

    def HandleEvent(self, event):
        for button in self.buttons:
            button.HandleEvent(event)

    def Draw(self, screen):
        screen.fill(("black"))
        screen.blit(self.endTitleSurf, self.endTitleRect)
        for button in self.buttons:
            button.Draw(screen)

    def ExitGame(self):
        self.game.running = False

    def RestartGame(self):
        self.game.ChangeScene(True, self.game.EndToMenu)
