import random


class Animal:
    def __init__(self, x, y, hungerSpeed, boredomSpeed):
        self.boredom = 100
        self.food = 100
        self.x = x
        self.y = y
        self.hungerSpeed = hungerSpeed
        self.boredomSpeed = boredomSpeed
        self.currentSide = None
        self.move = True

    def Feed(self):
        pass

    def Pet(self):
        pass

    def Move(self):
        if self.move:
            if self.currentSide is None:
                self.currentSide = random.choice(("left", "right"))

    def CheckBoredomAndFood(self):
        return self.boredom > 0 or self.food > 0

    def ReduceBoredomAndFood(self):
        self.boredom -= self.boredomSpeed
        self.food -= self.hungerSpeed
