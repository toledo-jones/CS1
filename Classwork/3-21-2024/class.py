class Fish:
    tank = "My Tank"

    def __init__(self):
        self.tank = "3rd tank"

    """
    Empty fish object
    Attributes will be filled out with declarations from wherever the object is instantiated
    """
    pass


fish1 = Fish()
fish1.name = "Nemo"
fish1.age = 7
# fish1.tank = "Different Tank"
print(f"fish1 is called {fish1.name}")
print(f"fish1 is {fish1.age} years old")
print(f"{fish1.name} is in {fish1.tank}")
print(f"Default Tank is {Fish.tank}")
