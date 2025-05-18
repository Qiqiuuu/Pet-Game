from Animals.Animal import Animal


class BlobFish(Animal):

    def __init__(self, x, y, hunger, boredom):
        path = f"../Animals/Pets/BlobFish/Assets/Blobfish Spritesheet_"
        animationsData = self.LoadAnimations(path)
        self.currentAnimationKey = "idle"
        super().__init__(x, y, hunger, boredom, animationsData, self.currentAnimationKey,
                         {"idle": ["idle"], "move": ["move"], "eat": ["eat"], "pet": ["pet"]})

    def LoadAnimations(self, path):
        animations = {
            "idle": [f"{path}01.png"],
            "eat": [f"{path}{i}.png" for i in range(12, 17)] + [f"{path}{i}.png" for i in range(16, 11, -1)],
            "pet": [f"{path}{i}.png" for i in range(19, 23)] + [f"{path}{i}.png" for i in range(22, 18, -1)],
            "move": [f"{path}{i}.png" if i >= 10 else f"{path}0{i}.png" for i in range(1, 12)]
        }
        return animations

    def Feed(self):
        super().Feed()

    def Pet(self):
        super().Pet()

    def Update(self, screen):
        super().Update(screen)

    def Draw(self, screen):
        super().Draw(screen, "right", scale=0.6)
