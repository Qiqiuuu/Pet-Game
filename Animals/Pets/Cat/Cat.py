import random

from Animals.Animal import Animal


class Cat(Animal):
    catType = ["hairless", "radioactive", "dark", "brown", "black", "white", "seal_point", "orange"]

    def __init__(self, x, y, hunger, boredom):
        self.choice = random.choice(Cat.catType)
        path = f"../Animals/Pets/Cat/Assets/{self.choice}/{self.choice}_"
        animationsData = self.LoadAnimations(path)
        self.currentAnimationKey = "idle"
        super().__init__(x, y, hunger, boredom, animationsData, self.currentAnimationKey,
                         {"idle": ["idle"], "move": ["run"], "eat": ["eat"], "pet": ["pet"]})

    def LoadAnimations(self, path):
        animations = {
            "idle": [f"{path}{i}.png" for i in range(96, 100)] + [f"{path}{i}.png" for i in range(128, 130)]
                    + [f"{path}129.png"] * 20,
            "eat": [f"{path}{i}.png" for i in range(96, 100)] +
                   [f"{path}{i}.png" for i in range(128, 130)] +
                   [f"{path}{i}.png" for i in range(100, 104)] +
                   [f"{path}132.png"],
            "pet": [f"{path}{i}.png" for i in range(96, 100)] +
                   [f"{path}{i}.png" for i in range(128, 130)] +
                   [f"{path}{i}.png" for i in range(104, 108)] +
                   [f"{path}{i}.png" for i in range(136, 140)],
            "walk": [f"{path}{i}.png" for i in range(108, 112)],
            "run": [f"{path}{i}.png" for i in range(116, 120)] + [f"{path}{i}.png" for i in range(148, 152)]
        }
        return animations

    def Feed(self):
        super().Feed()

    def Pet(self):
        super().Pet()

    def Update(self, screen):
        super().Update(screen)

    def Draw(self, screen):
        super().Draw(screen, "right", scale=0.7)
