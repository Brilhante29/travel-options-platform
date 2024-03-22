from core.utils.either import left, right
from core.errors.resource_not_found_error import ResourceNotFoundError
from travel_option_repository import TravelOptionRepository


class FindTravelOptionsByCityUseCase:
    def __init__(self, repository: TravelOptionRepository):
        self.repository = repository

    def execute(self, city: str):
        options = self.repository.find_by_city(city)
        if not options:
            return left(ResourceNotFoundError(f"No travel options found for city: {city}"))
        else:
            return right(options)