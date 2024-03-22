from src.infra.database.sqlite.repositories.sqlite_travel_option_repository import SqliteTravelOptionRepository
from src.domain.application.use_cases.find_most_comfortable_and_fastest_travel_option_for_city import (
    FindMostComfortableAndFastestTravelOptionForCityUseCase,
)
from src.infra.rest.controllers.get_most_comfortable_and_fastest_travel_option_for_city import (
    GetMostComfortableAndFastestTravelOptionByCityController,
)


def get_most_comfortable_and_fastest_travel_option_for_city_composer():
    repository = SqliteTravelOptionRepository()
    use_case = FindMostComfortableAndFastestTravelOptionForCityUseCase(repository)
    controller = GetMostComfortableAndFastestTravelOptionByCityController(use_case)

    return controller.execute
