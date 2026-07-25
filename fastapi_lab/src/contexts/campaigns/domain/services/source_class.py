from intermediate_class import IntermediateClass

class SourceClass:
    def __init__(self, intermediate_class: IntermediateClass):
        self._intermediate_class = intermediate_class

    def send_value(self):
        source_value = "Valor criado na SourceClass"

        self._intermediate_class.receive_value(source_value)
