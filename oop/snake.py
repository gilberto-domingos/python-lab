from oop.animal import Animal


class Snake(Animal):
    def __init__(self, name: str):
        super().__init__(name, "Rattlesnake", "Reptilia")

    def communicate(self) -> str:
        return f"The {self.name} rattle ! rattle ! rattle !"

    def behavior(self) -> str:
        return f"The {self.name} snake crawls on the ground"

    def __str__(self):
        return f"Snake(name={self.name}, kind={self.kind}, species={self.species})"
