from fastapi import APIRouter

from  src.infra.rest.routes import route_get_most_comfortable_and_fastest_travel_option_for_city, route_get_most_economical_travel_option_for_city, route_get_travel_option_by_city

api_router = APIRouter()

api_router.include_router(route_get_most_economical_travel_option_for_city.router, prefix="/economical", tags=["Economical Options"])
api_router.include_router(route_get_most_comfortable_and_fastest_travel_option_for_city.router, prefix="/fastest", tags=["Fastest Options"])
api_router.include_router(route_get_travel_option_by_city.router, prefix="/options", tags=["Options By City"])
