from source_class import SourceClass
from intermediate_class import IntermediateClass
from destination_class import DestinationClass

destination_class = DestinationClass()

intermediate_class = IntermediateClass(
    destination_class
)

source_class = SourceClass(
    intermediate_class
)

source_class.send_value()
