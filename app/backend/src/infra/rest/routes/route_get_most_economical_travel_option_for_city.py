from typing import List
from fastapi import APIRouter
from src.infra.rest.controllers.composer.composer_get_most_economical_travel_option_for_city import (
    get_most_economical_travel_option_for_city_composer,
)
from src.infra.rest.schemas.travel_option import TravelOptionModel

router = APIRouter()


@router.get("/travel-options/economical/{city}", response_model=List[TravelOptionModel])
async def route_get_most_economical_travel_option_by_city(city: str):
    controller_execute_function = get_most_economical_travel_option_for_city_composer()
    return await controller_execute_function(city)
