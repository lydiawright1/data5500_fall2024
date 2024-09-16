#animal bird is parent

class Bird:
    def __init__(self, species, color):
        self.species = species
        self.color = color
        
    
    def movement(self):
        return str(self.species) + " fly"

robin = Bird("Robin", "Brown and Red")

eagle = Bird("Eagle", "Brown and White")

class NotFlyBird(Bird):
    def movement(self):
        return str(self.species) + " waddle"
    
penguin = NotFlyBird("Penguin", "Black and White")

birds = [robin, eagle, penguin]

for bird in birds:
    print(bird.movement())