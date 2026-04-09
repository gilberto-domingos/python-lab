# =================================================
#    Information Security - Junior vs Senior
# =================================================
class Dog:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        if not value:
            raise ValueError("Cannot be empty")
        self._name = value

    def __str__(self):
        return f"(Dog={self.name})"


dog1 = Dog("Rex")
dog1.name = "Bob"
print(dog1.name)
