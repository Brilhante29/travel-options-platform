from typing import List
from fastapi import APIRouter
from src.infra.rest.controllers.composer.composer_get_travel_option_by_city import (
    get_travel_option_by_city_composer,
)
from src.infra.rest.schemas.travel_option import TravelOptionModel

router = APIRouter()


@router.get("/travel-options/{city}", response_model=List[TravelOptionModel])
async def route_get_travel_option_by_city(city: str):
    controller_execute_function = get_travel_option_by_city_composer()
    return await controller_execute_function(city)
