from typing import List, Optional
from src.core.repositories import (
    PaginatedResult,
    PaginationParams,
)
from src.domain.application.repositories.travel_option_repository import (
    TravelOptionRepository,
)
from  src.domain.enterprise.entities.travel_option import TravelOption


class InMemoryTravelOptionRepository(TravelOptionRepository):
    items: List[TravelOption] = []
    
    def _clear(self):
        self.items = []

    def save(self, entity: TravelOption) -> TravelOption:
        self.items.append(entity)
        return entity

    def find_all(self) -> List[TravelOption]:
        return self.items

    def find_all_paginated(
        self, pagination: PaginationParams
    ) -> PaginatedResult[TravelOption]:
        start = (pagination.page - 1) * pagination.limit
        end = start + pagination.limit
        paginated_items = self.items[start:end]
        return PaginatedResult(
            items=paginated_items,
            total=len(self.items),
            page=pagination.page,
            limit=pagination.limit,
        )

    def find_by_id(self, id: str) -> Optional[TravelOption]:
        for item in self.items:
            if str(item.id) == id:
                return item
        return None

    def update(self, id: str, entity: TravelOption) -> Optional[TravelOption]:
        for i, existing_item in enumerate(self.items):
            if str(existing_item.id) == id:
                self.items[i] = entity
                return entity
        return None

    def delete(self, id: str) -> None:
        self.items = [item for item in self.items if str(item.id) != id]

    def get_all_travel_options(self) -> List[TravelOption]:
        return self.items

    def find_by_city(self, city: str) -> List[TravelOption]:
        return [option for option in self.items if option.city.lower() == city.lower()]

    def find_most_economical_for_city(self, city: str) -> Optional[TravelOption]:
        city_options = [
            option for option in self.items if option.city.lower() == city.lower()
        ]
        if not city_options:
            return None
        return min(city_options, key=lambda x: x.price_econ)

    def find_most_comfortable_and_fastest_for_city(
        self, city: str
    ) -> Optional[TravelOption]:
        city_options = [
            option for option in self.items if option.city.lower() == city.lower()
        ]
        if not city_options:
            return None
        city_options.sort(
            key=lambda x: (x.price_confort, -self.__parse_duration(x.duration)),
            reverse=True,
        )
        return city_options[0] if city_options else None

    @staticmethod
    def __parse_duration(duration: str) -> int:
        """
        Helper function to convert duration string "Xh" into minutes for sorting.
        """
        hours = int(duration[:-1])
        return hours * 60
