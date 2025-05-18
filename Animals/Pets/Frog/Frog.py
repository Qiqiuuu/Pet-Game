import random

import pygame

from Animals.Animal import Animal


class Frog(Animal):
    frogType = ["blue", "brown", "GameBoy_B&W", "GameBoy_Green", "green", "purple"]

    def __init__(self, x, y, hunger, boredom):
        self.choice = random.choice(Frog.frogType)
        path = f"../Animals/Pets/Frog/Assets/frog_{self.choice}_spritesheet/frog_{self.choice}_spritesheet_"
        animationsData = self.LoadAnimations(path)
        self.currentAnimationKey = "idle1"
        super().__init__(x, y, hunger, boredom, animationsData, self.currentAnimationKey,
                         {"idle": ["idle1", "idle2"], "move": ["move"], "eat": ["eat"], "pet": ["pet"]})

    def LoadAnimations(self, path):
        animations = {
            "idle1": [f"{path}00.png", f"{path}08.png", f"{path}08.png"],
            "idle2": [f"{path}19.png", f"{path}27.png", f"{path}27.png"],
            "move": [f"{path}02.png", f"{path}10.png", f"{path}18.png", f"{path}26.png", f"{path}28.png",
                     f"{path}20.png", f"{path}12.png", f"{path}04.png"],
            "eat": [f"{path}00.png", f"{path}03.png", f"{path}03.png",f"{path}03.png",f"{path}03.png",f"{path}08.png"],
            "pet": [f"{path}01.png", f"{path}09.png", f"{path}17.png", f"{path}25.png", f"{path}17.png",
                    f"{path}25.png", f"{path}17.png", f"{path}09.png"],
        }
        return animations

    def Feed(self):
        super().Feed()

    def Pet(self):
        super().Pet()

    def Update(self, screen):
        super().Update(screen)

    def Draw(self, screen):
        super().Draw(screen,"right")
