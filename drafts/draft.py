class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


dog1 = Dog("Rex")
print(dog1)


# class Dog:
#     def __init__(self, name: str):
#         self._name = name
#
#     @property
#     def name(self) -> str:
#         return self._name
#
#     @name.setter
#     def name(self, value: str) -> None:
#         if not value:
#             raise ValueError("Cannot be empty")
#         self._name = value
#
#     def __str__(self):
#         return f"Dog(name={self._name})"
#
#
# dog1 = Dog("Rex")
# dog1.name = "Bob"
# print(dog1.name)
