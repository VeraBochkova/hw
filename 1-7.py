class FarmAnimals():
    def __init__(self, kind, color, size, age):
        self.kind = kind
        self.color = color
        self.size = size
        self.age = age

    def __str__(self):
        return str(dict(kind=self.kind, color=self.color, size=self.size, age=self.age))

class Animals(FarmAnimals):
    def __init__(self, kind, color, size, age, horns, milk):
        super().__init__(kind, color, size, age)
        self.horns = horns
        self.milk = milk

    def __str__(self):
        return str(dict(kind=self.kind, color=self.color, size=self.size, age=self.age, horns=self.horns, milk=self.milk))

class Birds(FarmAnimals):
    def __init__(self, kind, color, size, age, gender, eggs):
        super().__init__(kind, color, size, age)
        self.gender = gender
        self.eggs = eggs

    def __str__(self):
        return str(dict(kind=self.kind, color=self.color, size=self.size, age=self.age, gender=self.gender, eggs=self.eggs))

cow = Animals('cow', 'white', 'big', 10, 'yes', 'yes')
print(cow)
goat = Animals('goat', 'grey', 'medium', 7, 'yes', 'yes')
print(goat)
sheep = Animals('sheep', 'black', 'medium', 2, 'no', 'no')
print(sheep)
pig = Animals('pig', 'pink', 'medium', 4, 'no', 'no')
print(pig)
duck = Birds('duck', 'grey', 'little', 2, 'female', 'yes')
print(duck)
chicken = Birds('chicken', 'black', 'little', 2, 'female', 'yes')
print(chicken)
goose = Birds('goose', 'white', 'medium', 3, 'male', 'no')
print(goose)





