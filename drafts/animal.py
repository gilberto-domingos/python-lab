from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, kind: str, species: str):
        self._name = name
        self._kind = kind
        self._species = species

    @property
    def name(self) -> str:
        return self._name

    @property
    def kind(self) -> str:
        return self._kind

    @property
    def species(self) -> str:
        return self._species

    @name.setter
    def name(self, value) -> None:
        if not value:
            raise ValueError("Cannot be empty")
        self._name = value

    @kind.setter
    def kind(self, value: str) -> None:
        if not value:
            raise ValueError("Cannot be empty")
        self._kind = value

    @species.setter
    def species(self, value) -> None:
        if not value:
            raise ValueError("Cannot be empty")
        self._species = value

    @abstractmethod  # What sound does emit
    def communicate(self) -> str:
        pass

    @abstractmethod  # what behavior perform it
    def behavior(self) -> str:
        pass

    def __str__(self):
        return f"Animal(name={self._name}, kind={self._kind} species={self._species})"
