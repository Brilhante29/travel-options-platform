from fastapi import HTTPException, status
from src.domain.application.use_cases.find_travel_option_by_city import (
    FindTravelOptionsByCityUseCase,
)
from  src.infra.rest.presenteners.travel_option_presentener import TravelOptionPresentener


class GetTravelOptionByCityController:
    def __init__(self, use_case: FindTravelOptionsByCityUseCase):
        self.use_case = use_case

    async def execute(self, city: str):
        result = self.use_case.execute(city)
        if result.is_left():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=result.left_value.args[0]  # Supondo que UseCaseError usa args para armazenar a mensagem
            )
        # Verifique se result.right_value é uma lista e, se não, coloque-a em uma lista
        travel_option = result.right_value
        if not isinstance(travel_option, list):
            travel_option = [travel_option]
        return [TravelOptionPresentener.to_http(option) for option in travel_option]