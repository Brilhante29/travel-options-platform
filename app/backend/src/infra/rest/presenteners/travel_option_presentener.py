from src.domain.enterprise.entities.travel_option import TravelOption
from  src.infra.rest.schemas.travel_option import TravelOptionModel


class TravelOptionPresentener:
    @staticmethod
    def to_domain(model: TravelOptionModel):
        return TravelOption(
            name=model.name,
            price_confort=model.price_confort,
            price_econ=model.price_econ,
            city=model.city,
            duration=model.duration,
            seat=model.seat,
            bed=model.bed,
        )

    @staticmethod
    def to_http(entity: TravelOption):
        # Garanta que esta função retorne um dicionário ou objeto correspondente ao modelo Pydantic
        return TravelOptionModel(
            id=entity.id,  # Este campo está faltando na sua implementação atual
            name=entity.name,
            price_confort=entity.price_confort,
            price_econ=entity.price_econ,
            city=entity.city,
            duration=entity.duration,
            seat=entity.seat,
            bed=entity.bed,
        ).model_dump() 
