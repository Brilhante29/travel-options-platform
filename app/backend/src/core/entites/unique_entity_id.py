from abc import ABC

class UniqueEntityID(ABC):
    def __init__(self, value: int = None):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, UniqueEntityID):
            return False
        return self.value == other.value
