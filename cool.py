
class Cat:
    def __init__(self, size: float, color: str, paws: int, stripes: int):
        self.size = size
        self.color = color
        self.paws = paws
        self.stripes = stripes

class Tiger(Cat):
    def __init__(self, size: float, color: str, paws: int, stripes: int, rage: int):
        
        self.rage = rage
        self.size = size
        self.color = color
        self.paws = paws
        self.stripes = stripes


class Kitty(Cat):
    def __init__(self,size: float, color: str, paws: int, stripes: int, happiness: int, name: str):

        self.happiness = happiness
        self.name = name
        self.size = size
        self.color = color
        self.paws = paws
        self.stripes = stripes

White_tiger = Tiger(210.23, "White", 4, 20, 100)
house_cat = Kitty(10, "Black", 4, 0, 100, "Fluffy")

print("White Tiger:", "size:",  White_tiger.size, "color:", White_tiger.color, "paws:",  White_tiger.paws, "Stripes:", White_tiger.stripes, 'rage:', White_tiger.rage)
print("House Cat:", "size:" , house_cat.size, "color:", house_cat.color, "paws:", house_cat.paws, "Stripes:", house_cat.stripes, "happiness:", house_cat.happiness,"name:", house_cat.name)


