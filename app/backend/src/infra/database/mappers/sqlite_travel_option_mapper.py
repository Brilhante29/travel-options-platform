from  src.domain.enterprise.entities.travel_option import TravelOption


class SqliteTravelOptionMapper:
    @staticmethod
    def to_domain(raw: dict) -> TravelOption:
        """
        Convert raw data (e.g., from database) into a TravelOption domain entity.
        """
        return TravelOption(
            id=raw.get("id"),
            name=raw.get("name"),
            price_confort=float(raw.get("price_confort").replace("R$", "").replace(",", ".")) if isinstance(raw.get("price_confort"), str) else raw.get("price_confort"),
            price_econ=float(raw.get("price_econ").replace("R$", "").replace(",", ".")) if isinstance(raw.get("price_econ"), str) else raw.get("price_econ"),
            city=raw.get("city"),
            duration=raw.get("duration"),
            seat=raw.get("seat"),
            bed=raw.get("bed"),
        )

    @staticmethod
    def to_db(travel_option: TravelOption) -> dict:
        """
        Convert a TravelOption domain entity into a persistence-ready format (e.g., for database storage).
        """
        return {
            "id": travel_option.id.value if travel_option.id else None,
            "name": travel_option.name,
            "price_confort": f"R$ {travel_option.price_confort:.2f}".replace(".", ","),
            "price_econ": f"R$ {travel_option.price_econ:.2f}".replace(".", ","),
            "city": travel_option.city,
            "duration": travel_option.duration,
            "seat": travel_option.seat,
            "bed": travel_option.bed,
        }
