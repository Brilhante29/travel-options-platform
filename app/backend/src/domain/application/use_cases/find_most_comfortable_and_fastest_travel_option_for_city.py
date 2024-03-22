from src.core.errors.invalid_input_error import InvalidInputError
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.utils.either import left, right
from src.domain.application.repositories.travel_option_repository import TravelOptionRepository


class FindMostComfortableAndFastestTravelOptionForCityUseCase:
    def __init__(self, repository: TravelOptionRepository):
        self.repository = repository

    def execute(self, city: str):
        if not city:
            return left(InvalidInputError("City must be provided"))
        option = self.repository.find_most_comfortable_and_fastest_for_city(city)
        if option is None:
            return left(ResourceNotFoundError(f"No comfortable and fastest travel option found for city: {city}"))
        else:
            return right(option)
