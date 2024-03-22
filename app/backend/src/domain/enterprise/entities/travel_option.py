from core.entites.entity import Entity
from core.entites.unique_entity_id import UniqueEntityID


class TravelOption(Entity):
    def __init__(
        self,
        name: str,
        price_confort: float,
        price_econ: float,
        city: str,
        duration: str,
        seat: str,
        bed: str,
        id: int = None,  
    ):
        super().__init__(UniqueEntityID(id) if id is not None else None)
        self.name = name
        self.price_confort = price_confort
        self.price_econ = price_econ
        self.city = city
        self.duration = duration
        self.seat = seat
        self.bed = bed

    def __eq__(self, other):
        if not isinstance(other, TravelOption):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id.value)

    @property
    def to_dict(self):
        return {
            "id": self.id.value,
            "name": self.name,
            "price_confort": self.price_confort,
            "price_econ": self.price_econ,
            "city": self.city,
            "duration": self.duration,
            "seat": self.seat,
            "bed": self.bed,
        }
