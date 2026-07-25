from destination_class import DestinationClass

class IntermediateClass:
    def __init__(self, destination_class: DestinationClass):
        self._destination_class  = destination_class

    def receive_value(self, source_value: str) -> str:
        intermediate_value = source_value

        self._destination_class.receive_value(intermediate_value)