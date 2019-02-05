class Food:
    name = "Pad Thai"
    cuisine = "Thai"

    def __init__(self, name="Burger", cuisine="American"):
        self.name = name
        self.cuisine = cuisine

    def __repr__(self):
        return "{} is {}.".format(self.name, self.cuisine)

    @staticmethod
    def static_describe(name, cuisine):
        print("{} is {}.".format(name, cuisine))

    @classmethod
    def class_describe(cls):
        print("{} is {}.".format(cls.name, cls.cuisine))

    def describe(self):
        print("{} is {}.".format(self.name, self.cuisine))


class Meat(Food):
    def cook(self):
        print("Cooking {}!".format(self.name))


class Fruit(Food):
    def clean(self):
        print("Cleaning {}!".format(self.name))


food = Food("Burger", "American")
food.describe()
print(food)
print()
orange = Fruit("Orange", "Citrus")
orange.describe()
orange.clean()
print(orange)
print()
meat = Meat("Beef", "Cow")
meat.describe()
meat.cook()
print(meat)
