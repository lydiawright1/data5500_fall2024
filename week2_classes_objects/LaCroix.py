class LaCroix:
    def __init__(self, flavor, color, yumminess):
        self.flavor = flavor
        self.color = color
        self.yumminess = yumminess
    
    def __str__(self):
        return "This La Croix Flavor is " + self.flavor + ", and it is " + str(self.yumminess) + "/10 on the yumminess scale. If you want to purchase it, look for the " + self.color + " can."
    

razz_cranberry = LaCroix("Razz-Cranberry", "Pink", 8)

print(razz_cranberry)