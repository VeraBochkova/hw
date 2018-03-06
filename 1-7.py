class FarmAnimals():
    def __init__(self, name, color, size, age):
        self.name = name
        self.color = color
        self.size = size
        self.age = age

    def __str__(self):
        return str(dict(name=self.name, color=self.color, size=self.size, age=self.age))


class Animals(FarmAnimals):
    def __init__(self, name, color, size, age, legs):
        super().__init__(name, color, size, age)
        self.legs = legs

    def __str__(self):
        return str(dict(name=self.name, color=self.color, size=self.size, age=self.age, legs=self.legs))


class Birds(FarmAnimals):
    def __init__(self, name, color, size, age, wings):
        super().__init__(name, color, size, age)
        self.wings = wings

    def __str__(self):
        return str(dict(name=self.name, color=self.color, size=self.size, age=self.age, wings=self.wings))



class Cows(Animals):
    def __init__(self, name, color, size, age, legs, milk):
        super().__init__(name, color, size, age, legs)
        self.milk = milk

    def __str__(self):
        return str(dict(name=self.name, color=self.color, size=self.size, age=self.age, legs=self.legs, milk=self.milk))


class Goats(Animals):
    def __init__(self, name, color, size, age, legs, horns):
        super().__init__(name, color, size, age, legs)
        self.horns = horns

    def __str__(self):
        return str(dict(name=self.name, color=self.color, size=self.size, age=self.age, legs=self.legs, horns=self.horns))


class Sheep(Animals):
    def __init__(self, name, color, size, age, legs, wool):
        super().__init__(name, color, size, age, legs)
        self.wool = wool

    def __str__(self):
        return str(dict(name=self.name, color=self.color, size=self.size, age=self.age, legs=self.legs, wool=self.wool))


class Pigs(Animals):
    def __init__(self, name, color, size, age, legs, meet):
        super().__init__(name, color, size, age, legs)
        self.meet = meet

    def __str__(self):
        return str(dict(name=self.name, color=self.color, size=self.size, age=self.age, legs=self.legs, meet=self.meet))


class Ducks(Birds):
    def __init__(self, name, color, size, age, wings, feather):
        super().__init__(name, color, size, age, wings)
        self.feather = feather

    def __str__(self):
        return str(dict(name=self.name, color=self.color, size=self.size, age=self.age, wings=self.wings, feather=self.feather))


class Chicken(Birds):
    def __init__(self, name, color, size, age, wings, eggs):
        super().__init__(name, color, size, age, wings)
        self.eggs = eggs

    def __str__(self):
        return str(dict(name=self.name, color=self.color, size=self.size, age=self.age, wings=self.wings, eggs=self.eggs))


class Geese(Birds):
    def __init__(self, name, color, size, age, wings, fluff):
        super().__init__(name, color, size, age, wings)
        self.fluff = fluff

    def __str__(self):
        return str(dict(name=self.name, color=self.color, size=self.size, age=self.age, wings=self.wings, fluff=self.fluff))


cow = Cows('Noosha', 'white', 'big', 10, 4, 'yes')
print(cow)
goat = Goats('Gena', 'grey', 'medium', 7, 4, 'yes')
print(goat)
sheep = Sheep('Masha', 'black', 'medium', 2, 4, 'yes')
print(sheep)
pig = Pigs('Noora', 'pink', 'medium', 4, 4, 'yes')
print(pig)
duck = Ducks('Donald', 'grey', 'little', 2, 2, 'yes')
print(duck)
chicken = Chicken('Natasha', 'black', 'little', 2, 2, 'yes')
print(chicken)
goose = Geese('Vasya', 'white', 'medium', 3, 2, 'yes')
print(goose)
goose1 = Geese('Venya', 'white', 'medium', 5, 2, 'no')
print(goose1)




