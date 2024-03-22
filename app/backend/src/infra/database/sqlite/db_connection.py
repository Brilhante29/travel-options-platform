import sqlite3


class DatabaseConnection:
    _instance = None

    def __new__(cls, db_path):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect(db_path, check_same_thread=False)
            cls._instance.cursor = cls._instance.connection.cursor()
        return cls._instance

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
