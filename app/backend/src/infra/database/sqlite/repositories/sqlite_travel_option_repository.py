import os
import sqlite3
from typing import List, Optional
from  src.infra.database.sqlite.db_connection import DatabaseConnection
from  src.core.repositories.pagination import PaginatedResult, PaginationParams
from  src.domain.application.repositories.travel_option_repository import (
    TravelOptionRepository,
)
from src.domain.enterprise.entities.travel_option import TravelOption


class SqliteTravelOptionRepository(TravelOptionRepository):
    def __init__(self):
        current_directory = os.path.dirname(__file__)
        db_path = os.path.join(current_directory, '../../travel_options.db')
        self.db = DatabaseConnection(db_path)

    def _get_connection(self):
        return self.db.connection

    def _dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def save(self, entity: TravelOption) -> TravelOption:
        # Exemplo de implementação; ajuste conforme sua estrutura e necessidades
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO travel_options (name, price_confort, price_econ, city, duration, seat, bed)
                          VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                entity.name,
                entity.price_confort,
                entity.price_econ,
                entity.city,
                entity.duration,
                entity.seat,
                entity.bed,
            ),
        )
        conn.commit()
        return entity

    def find_all(self) -> List[TravelOption]:
        conn = self._get_connection()
        conn.row_factory = self._dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM travel_options")
        return [TravelOption(**option) for option in cursor.fetchall()]

    def find_all_paginated(
        self, pagination: PaginationParams
    ) -> PaginatedResult[TravelOption]:
        conn = self._get_connection()
        conn.row_factory = self._dict_factory
        cursor = conn.cursor()

        # Calculando o ponto de partida com base na página e no limite
        offset = (pagination.page - 1) * pagination.limit

        # Buscando a quantidade total de registros para calcular o total de páginas
        cursor.execute("SELECT COUNT(*) as total FROM travel_options")
        total = cursor.fetchone()["total"]

        cursor.execute(
            "SELECT * FROM travel_options LIMIT ? OFFSET ?", (pagination.limit, offset)
        )
        items = [TravelOption(**option) for option in cursor.fetchall()]

        total_pages = (total // pagination.limit) + (
            1 if total % pagination.limit > 0 else 0
        )

        return PaginatedResult(
            items=items,
            total=total,
            page=pagination.page,
            limit=pagination.limit,
            total_pages=total_pages,
        )

    def find_by_id(self, id: str) -> Optional[TravelOption]:
        conn = self._get_connection()
        conn.row_factory = self._dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM travel_options WHERE id = ?", (id,))
        result = cursor.fetchone()
        
        return TravelOption(**result) if result else None

    def find_by_city(self, city: str) -> List[TravelOption]:
        conn = self._get_connection()
        conn.row_factory = self._dict_factory
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM travel_options WHERE lower(city) = lower(?)", (city,)
        )
        return [TravelOption(**option) for option in cursor.fetchall()]

    def find_most_economical_for_city(self, city: str) -> Optional[TravelOption]:
        conn = self._get_connection()
        conn.row_factory = self._dict_factory
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM travel_options WHERE lower(city) = lower(?) ORDER BY price_econ ASC LIMIT 1",
            (city,),
        )
        result = cursor.fetchone()
        return TravelOption(**result) if result else None


    def find_most_comfortable_and_fastest_for_city(self, city: str) -> Optional[TravelOption]:
        conn = self._get_connection()
        conn.row_factory = self._dict_factory
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *, CAST(SUBSTR(duration, 1, LENGTH(duration) - 1) AS INTEGER) AS duration_hours 
            FROM travel_options 
            WHERE lower(city) = lower(?) 
            ORDER BY price_confort DESC, duration_hours ASC 
            LIMIT 1
            """,
            (city,),
        )

        result = cursor.fetchone()
        if result:
            # Remova o campo 'duration_hours' antes de passar para a inicialização de TravelOption
            result.pop('duration_hours', None)
            return TravelOption(**result)
        return None
    
    
    def update(self, id: str, entity: TravelOption) -> TravelOption:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE travel_options 
               SET name=?, price_confort=?, price_econ=?, city=?, duration=?, seat=?, bed=?
               WHERE id=?""",
            (
                entity.name,
                entity.price_confort,
                entity.price_econ,
                entity.city,
                entity.duration,
                entity.seat,
                entity.bed,
                id
            ),
        )
        conn.commit()
        return entity

    def delete(self, id: str) -> None:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM travel_options WHERE id = ?",
            (id,)
        )
        conn.commit()
