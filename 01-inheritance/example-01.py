class Animal:
    def __init__(self, name):
        self.name = name

    def sample(self):
        print("Sub-class calling base method")

    @property
    def my_name(self):
        print( f"My name is {self.name}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    @property
    def my_name(self):
        return f"i am dog with name {self.name}"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    @property
    def my_name(self):
        return f"i am a cat with name {self.name}"


if __name__ == "__main__":
    dog = Dog("Bingo")
    cat = Cat("pinky")
    dog.sample()
    print(dog.my_name)
    print(cat.my_name)

    issubclass(Dog, Animal) # True
    issubclass(Animal, object) # True
    isinstance(dog, Dog) # True
    isinstance(cat, object) # True


