import pygame

from Animals import BlobFish
from Animals import Frog
from Animals import Cow
from Slider import Slider
from Button import Button
import Animals


class Menu:
    def __init__(self, game):
        self.game = game
        self.width = game.width
        self.height = game.height
        self.font = pygame.font.Font(None, int(36 * (self.width / 800)))
        self.title_font = pygame.font.Font(None, int(74 * (self.width / 800)))
        self.menuTitle = self.CreateTextRect("Game Menu", self.title_font, 0.5, 0.1)
        self.foodSlider = Slider(self.width / 2, self.height / 2 - self.height * 0.01, self.width * 0.25,
                                 self.height * 0.07)
        self.boredomSlider = Slider(self.width / 2, self.height / 2 - self.height * 0.2, self.width * 0.25,
                                    self.height * 0.07)
        self.foodTextSurface = self.font.render(f"Food drop rate: {self.foodSlider.GetValue()}", True, (255, 255, 255))
        self.foodTextRect = self.foodTextSurface.get_rect(
            centerx=int(self.foodSlider.rect.centerx),
            bottom=int(self.foodSlider.rect.top - self.width * 0.005)
        )

        self.boredomTextSurface = self.font.render(f"Boredom drop rate: {self.boredomSlider.GetValue()}", True,
                                                   (255, 255, 255))
        self.boredomTextRect = self.boredomTextSurface.get_rect(
            centerx=int(self.boredomSlider.rect.centerx),
            bottom=int(self.boredomSlider.rect.top - self.width * 0.005)
        )

        self.buttons = []
        self.CreateButtonGrid()

    def CreateTextRect(self, text, font, xPercent, yPercent):
        surface = font.render(text, True, (255, 255, 255))
        rect = surface.get_rect(
            center=(int(self.width * xPercent), int(self.height * yPercent)))
        return surface, rect

    def HandleEvent(self, event):
        self.foodSlider.HandleEvent(event)
        self.boredomSlider.HandleEvent(event)
        for button in self.buttons:
            button.HandleEvent(event)

    def Update(self):
        self.foodTextSurface = self.font.render(f"Food drop rate: {self.foodSlider.GetValue()}", True, (255, 255, 255))
        self.boredomTextSurface = self.font.render(f"Boredom drop rate: {self.boredomSlider.GetValue()}", True,
                                                   (255, 255, 255))

    def Draw(self, screen):
        screen.fill((50, 50, 50))
        self.foodSlider.Draw(screen)
        self.boredomSlider.Draw(screen)
        screen.blit(self.foodTextSurface, self.foodTextRect)
        screen.blit(self.boredomTextSurface, self.boredomTextRect)
        screen.blit(self.menuTitle[0], self.menuTitle[1])
        for button in self.buttons:
            button.Draw(screen)

    def CreateButtonGrid(self):
        buttonWidth = self.width * 0.15
        buttonHeight = self.height * 0.1
        buttonSpacingX = buttonWidth // 5
        buttonSpacingY = buttonWidth // 5

        gridWidth = 2 * buttonWidth + buttonSpacingX
        gridHeight = 2 * buttonHeight + buttonSpacingY

        gridX = (self.width - gridWidth) / 2
        gridY = (self.height - gridHeight) / 2 + self.height*0.25

        button_texts = ["Cow", "Cat", "Frog", "Blob fish"]
        actions = [lambda: self.game.SetPet(
            Cow(self.width / 2, self.height * 0.5, self.foodSlider.GetValue(), self.boredomSlider.GetValue())),
                   lambda: self.game.SetPet(Cow(self.width / 2, self.height * 0.7, self.foodSlider.GetValue(), self.boredomSlider.GetValue())),
                   lambda: self.game.SetPet(Frog(self.width / 2, self.height * 0.6, self.foodSlider.GetValue(), self.boredomSlider.GetValue())),
                   lambda: self.game.SetPet(BlobFish(self.width / 2, self.height * 0.6, self.foodSlider.GetValue(), self.boredomSlider.GetValue()))]
        buttonIndex = 0

        for row in range(2):
            for col in range(2):
                x = gridX + col * (buttonWidth + buttonSpacingX) + buttonWidth / 2
                y = gridY + row * (buttonHeight + buttonSpacingY) + buttonHeight / 2
                button = Button(x, y, buttonWidth, buttonHeight, button_texts[buttonIndex], actions[buttonIndex])
                self.buttons.append(button)
                buttonIndex += 1
