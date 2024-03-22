from .unique_entity_id import UniqueEntityID
from abc import ABC


class Entity(ABC):
    def __init__(self, id: UniqueEntityID = None):
        self._id = id or UniqueEntityID()

    @property
    def id(self):
        return self._id

    def __eq__(self, other):
        if other is None or not isinstance(other, Entity):
            return False
        if other is self:
            return True
        return self._id == other.id
