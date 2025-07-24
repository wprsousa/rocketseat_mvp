"""
Imaginando como funciona o SQLAlchemy, podemos pensar numa pessoa que quer acessar um banco de dados.

1 - Criamos a engine (motor) para conexão.
2 - Abrimos uma sessão, ou seja, o momento em que estou disponível para interagir com o banco.
3 - Com isso vou de fato conseguir fazer os comandos sql no banco.
"""

from sqlalchemy import create_engine
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    def __init__(self, connection_string: str = "sqlite:///storage.db") -> None:
        self.__connection_string = connection_string
        self.__engine: Engine | None = None
        self.session = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)

    @property
    def engine(self) -> Engine:
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


db_connection_handler = DBConnectionHandler()
