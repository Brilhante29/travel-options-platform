import os
import json
from src.infra.database.sqlite.db_connection import DatabaseConnection

def init_db():
    # O caminho do diretório atual onde este script está localizado
    current_directory = os.path.dirname(__file__)
    
    # Subir três níveis para chegar ao diretório 'app'
    app_directory = os.path.abspath(os.path.join(current_directory, '../../../../../'))
    
    # O arquivo DB está na mesma pasta que este script
    db_path = os.path.join(current_directory, 'travel_options.db')
    db = DatabaseConnection(db_path)
    cursor = db.get_cursor()

    # Criando a tabela, se não existir
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS travel_options (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        price_confort REAL,
                        price_econ REAL,
                        city TEXT,
                        duration TEXT,
                        seat TEXT,
                        bed TEXT
                      )"""
    )

    # O arquivo JSON está no diretório 'app'
    json_path = os.path.join(app_directory, 'data.json')
    with open(json_path, "r", encoding="utf-8") as file:
        travel_options_data = json.load(file)
        travel_options = travel_options_data["transport"]

    cursor.execute("DELETE FROM travel_options")

    # Inserindo os dados no banco de dados usando o ID fornecido no JSON
    for option in travel_options:
        cursor.execute(
            """INSERT INTO travel_options (id, name, price_confort, price_econ, city, duration, seat, bed)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                option["id"],  # Usando o ID do JSON
                option["name"],
                float(option["price_confort"].replace('R$ ', '').replace(',', '.')),  # Convertendo para float e removendo o 'R$'
                float(option["price_econ"].replace('R$ ', '').replace(',', '.')),  # Convertendo para float e removendo o 'R$'
                option["city"],
                option["duration"],
                option["seat"],
                option["bed"],
            ),
        )

    db.commit()
