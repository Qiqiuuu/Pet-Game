import random

from Animals.Animal import Animal


class Cow(Animal):
    cowType = ["beige", "brown", "black", "grey", "white", "white_darkspots", "white_pinkspots"]

    def __init__(self, x, y, hunger, boredom):
        self.choice = random.choice(Cow.cowType)
        path = f"../Animals/Pets/Cow/Assets/cows_spritesheet_{self.choice}/cows_spritesheet_{self.choice}_"
        animationsData = self.LoadAnimations(path)
        self.currentAnimationKey = "idle"
        super().__init__(x, y, hunger, boredom, animationsData, self.currentAnimationKey,
                         {"idle": ["idle"], "move": ["move"], "eat": ["eat"], "pet": ["pet"]})

    def LoadAnimations(self, path):
        animations = {
            "idle": [f"{path}00.png", f"{path}01.png", f"{path}02.png", f"{path}04.png", f"{path}05.png"],
            "eat": [f"{path}{i}.png" if i >= 10 else f"{path}0{i}.png" for i in range(8, 16)],
            "pet": [f"{path}{i}.png" if i >= 10 else f"{path}0{i}.png" for i in range(8, 16)],
            "move": [f"{path}{i}.png" for i in range(17, 20)]
        }
        return animations

    def Feed(self):
        super().Feed()

    def Pet(self):
        super().Pet()

    def Update(self, screen):
        super().Update(screen)

    def Draw(self, screen):
        super().Draw(screen,"left",scale=0.8)
