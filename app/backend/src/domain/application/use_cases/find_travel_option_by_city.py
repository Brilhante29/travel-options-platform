from src.core.utils.either import left, right
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.application.repositories.travel_option_repository import TravelOptionRepository


class FindTravelOptionsByCityUseCase:
    def __init__(self, repository: TravelOptionRepository):
        self.repository = repository

    def execute(self, city: str):
        options = self.repository.find_by_city(city)
        if not options:
            return left(ResourceNotFoundError(f"No travel options found for city: {city}"))
        else:
            return right(options)