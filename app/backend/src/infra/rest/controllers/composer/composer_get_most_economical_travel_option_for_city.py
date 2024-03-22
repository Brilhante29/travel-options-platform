from src.infra.database.sqlite.repositories.sqlite_travel_option_repository import SqliteTravelOptionRepository
from src.domain.application.use_cases.find_most_economical_travel_option_for_city import (
    FindMostEconomicalTravelOptionForCityUseCase,
)
from src.infra.rest.controllers.get_most_economical_travel_option_for_city import (
    GetMostEconomicalTravelOptionForCityController,
)


def get_most_economical_travel_option_for_city_composer():
    repository = SqliteTravelOptionRepository()
    use_case = FindMostEconomicalTravelOptionForCityUseCase(repository)
    controller = GetMostEconomicalTravelOptionForCityController(use_case)

    return controller.execute
