from src.infra.database.sqlite.repositories.sqlite_travel_option_repository import SqliteTravelOptionRepository
from src.domain.application.use_cases.find_travel_option_by_city import (
    FindTravelOptionsByCityUseCase,
)
from  src.infra.rest.controllers.get_travel_option_by_city import (
    GetTravelOptionByCityController,
)


def get_travel_option_by_city_composer():
    repository = SqliteTravelOptionRepository()
    use_case = FindTravelOptionsByCityUseCase(repository)
    controller = GetTravelOptionByCityController(use_case)

    return controller.execute
