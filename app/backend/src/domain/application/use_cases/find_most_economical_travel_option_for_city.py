from core.errors.invalid_input_error import InvalidInputError
from core.errors.resource_not_found_error import ResourceNotFoundError
from core.utils.either import left, right
from travel_option_repository import TravelOptionRepository


class FindMostEconomicalTravelOptionForCityUseCase:
    def __init__(self, repository: TravelOptionRepository):
        self.repository = repository

    def execute(self, city: str):
        if not city:
            return left(InvalidInputError("City must be provided"))
        option = self.repository.find_most_economical_for_city(city)
        if option is None:
            return left(ResourceNotFoundError(f"No economical travel option found for city: {city}"))
        else:
            return right(option)