from drafts.animal import Animal


class Snake(Animal):
    def __init__(self, name: str):
        self._name = name
        super().__init__(name, "Rattlesnake", "Reptilia")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot be empty")
        self._name = value

    def communicate(self) -> str:
        return f"The {self.name} rattle!, rattle!, rattle!"

    def behavior(self) -> str:
        return f"The {self.name} snake crawls on the ground"

    def __str__(self):
        return f"Snake(name={self.name}, kind={self.kind}, species={self.species})"
