import pygame

from Animals.Pets.BlobFish.BlobFish import BlobFish
from Animals.Pets.Cat.Cat import Cat
from Animals.Pets.Frog.Frog import Frog
from Animals.Pets.Cow.Cow import Cow
from Slider import Slider
from ButtonIMG import ButtonIMG


class Menu:
    def __init__(self, game):
        self.game = game
        self.width = game.width
        self.height = game.height


        self.fontMP = 0.02
        self.titleFontMP = 0.08
        self.textXMP = 0.005
        self.sliderXMP = 0.25
        self.sliderYMP = 0.07
        self.foodSliderY = 0.02
        self.boredomSliderY = 0.15


        self.background = pygame.transform.scale(pygame.image.load("Assets/Background/Background.png"),
                                                 (self.width, self.height))

        self.font = pygame.font.Font("Assets/Minecraft.ttf", int(self.width * self.fontMP))
        self.titleFont = pygame.font.Font("Assets/Minecraft.ttf", int(self.width * self.titleFontMP))

        self.menuTitle = self.CreateTextRect("Game Menu", self.titleFont, 0.5, 0.15)
        self.shoutout = self.CreateTextRect("try also s30647", self.font, 0.65, 0.15, "yellow")

        self.foodSlider = Slider(self.width / 2, self.height / 2 + self.height * self.foodSliderY, self.width * self.sliderXMP,
                                 self.height * self.sliderYMP)

        self.foodTextSurface = self.font.render(f"Food drop rate: {self.foodSlider.GetValue()}", True, (255, 255, 255))
        self.foodTextRect = self.foodTextSurface.get_rect(
            centerx=int(self.foodSlider.rectSlider.centerx),
            bottom=int(self.foodSlider.rectSlider.top - self.width * self.textXMP)
        )
        self.boredomSlider = Slider(self.width / 2, self.height / 2 - self.height * self.boredomSliderY, self.width * self.sliderXMP,
                                    self.height * self.sliderYMP)
        self.boredomTextSurface = self.font.render(f"Boredom drop rate: {self.boredomSlider.GetValue()}", True,
                                                   (255, 255, 255))
        self.boredomTextRect = self.boredomTextSurface.get_rect(
            centerx=int(self.boredomSlider.rectSlider.centerx),
            bottom=int(self.boredomSlider.rectSlider.top - self.width * self.textXMP)
        )

        self.buttons = []
        self.CreateButtonGrid()

    def CreateTextRect(self, text, font, xPercent, yPercent, color=(255, 255, 255)):
        surface = font.render(text, True, color)
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
        screen.blit(self.background, (0, 0))
        self.foodSlider.Draw(screen)
        self.boredomSlider.Draw(screen)
        screen.blit(self.foodTextSurface, self.foodTextRect)
        screen.blit(self.boredomTextSurface, self.boredomTextRect)
        screen.blit(self.menuTitle[0], self.menuTitle[1])
        screen.blit(pygame.transform.rotate(self.shoutout[0], 25), self.shoutout[1])
        for button in self.buttons:
            button.Draw(screen)

    def CreateButtonGrid(self):
        buttonWidth = self.width * 0.15
        buttonHeight = self.height * 0.08
        buttonSpacingX = buttonWidth / 10
        buttonSpacingY = buttonWidth / 10

        gridWidth = 2 * buttonWidth + buttonSpacingX
        gridHeight = 2 * buttonHeight + buttonSpacingY

        gridX = (self.width - gridWidth) / 2
        gridY = (self.height - gridHeight) / 2 + self.height * 0.25

        buttonTexts = ["Cow", "Cat", "Frog", "Blob fish"]
        actions = [lambda: self.game.SetPet(
            Cow(self.width / 2, self.height * 0.5, self.foodSlider.GetValue(), self.boredomSlider.GetValue())),
                   lambda: self.game.SetPet(Cat(self.width / 2, self.height * 0.6, self.foodSlider.GetValue(),
                                                self.boredomSlider.GetValue())),
                   lambda: self.game.SetPet(Frog(self.width / 2, self.height * 0.6, self.foodSlider.GetValue(),
                                                 self.boredomSlider.GetValue())),
                   lambda: self.game.SetPet(BlobFish(self.width / 2, self.height * 0.6, self.foodSlider.GetValue(),
                                                     self.boredomSlider.GetValue()))]
        buttonIndex = 0

        for row in range(2):
            for col in range(2):
                x = gridX + col * (buttonWidth + buttonSpacingX) + buttonWidth / 2
                y = gridY + row * (buttonHeight + buttonSpacingY) + buttonHeight / 2
                button = ButtonIMG(x, y, buttonWidth, buttonHeight, buttonTexts[buttonIndex], actions[buttonIndex],
                                   image="Assets/button.png",
                                   imageHigh="Assets/button_highlighted.png")
                self.buttons.append(button)
                buttonIndex += 1
