from Animals.Animal import Animal


class Cow(Animal):
    def __init__(self,x=100,y=200,hunger = 50, bore = 50):
        super().__init__(x,y,hunger,bore)
