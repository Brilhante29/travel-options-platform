from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.repositories.crud_repository import CrudRepository
from src.domain.enterprise.entities.travel_option import TravelOption


class TravelOptionRepository(CrudRepository[TravelOption, str], ABC):
    @abstractmethod
    def find_by_city(self, city: str) -> List[TravelOption]:
        ...

    @abstractmethod
    def find_most_economical_for_city(self, city: str) -> Optional[TravelOption]:
        ...

    @abstractmethod
    def find_most_comfortable_and_fastest_for_city(
        self, city: str
    ) -> Optional[TravelOption]:
        ...
