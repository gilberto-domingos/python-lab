from oop.animal import Animal


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name, "Dog", "Mammalia")

    def communicate(self) -> str:
        return f"The {self.name} barks and Grlll ! grlll! grllll ! to attack !"

    def behavior(self) -> str:
        return f"The {self.name} runs to play !"

    def __str__(self):
        return f"Dog(name={self.name}, kind={self.kind}, species={self.species})"
