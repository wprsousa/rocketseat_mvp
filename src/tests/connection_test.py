import pytest
from sqlalchemy.engine import Engine
from src.models.sqlite.settings.connection import db_connection_handler


# teste de integração com o banco de dados | Não é um teste unitário
@pytest.mark.skip(reason="interação com o banco")
def test_connect_to_db():
    assert db_connection_handler.engine is None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.engine

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
