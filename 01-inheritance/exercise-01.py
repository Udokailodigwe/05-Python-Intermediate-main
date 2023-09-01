class Animal:
    def __init__(self, name, age):
        self.my_name = name
        self.my_age = age

    @property
    def name(self):
        return f"{self.my_name} is an animal"

    @property
    def age(self):
        return f"{self.my_name} is an animal and its {self.my_age} years old"

    @property
    def make_a_sound(self):
        return ""


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def name(self):
        return f"i am {self.my_name} the dog"

    @property
    def age(self):
        return f"i am {self.my_age} years old."

    #@property
    def make_a_sound(self):
        return "woof"


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def name(self):
        return f"i am {self.my_name} the cat"

    @property
    def age(self):
        return f"i am {self.my_age} years old."

    #@property
    def make_a_sound(self):
        return "meew"


if __name__ == "__main__":
    animal = Animal("lion", 6)
    dog = Dog("Bingo", 5)
    cat = Cat("Teddy", 3)

    print(animal.name)
    print(animal.my_name, animal.my_age)
    print(dog.my_name)
    print(dog.name)
    print(cat.my_name)
    print(cat.name)
    print(cat.age)
    print(dog.name, dog.age, dog.make_a_sound())
    print(cat.name, cat.age, cat.make_a_sound())
