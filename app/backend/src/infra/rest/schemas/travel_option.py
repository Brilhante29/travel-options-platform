from pydantic import BaseModel
from typing import Optional


class TravelOptionModel(BaseModel):
    name: str
    price_confort: float
    price_econ: float
    city: str
    duration: str
    seat: Optional[str] = None
    bed: Optional[str] = None