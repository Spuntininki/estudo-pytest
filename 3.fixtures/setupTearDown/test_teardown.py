import pytest
import sqlalchemy
from sqlalchemy.sql import text

@pytest.fixture
def database_connection():
    engine = sqlalchemy.create_engine('sqlite:///:memory:')
    conn = engine.connect()
    yield conn
    conn.close()
    
def test_database_connection(database_connection):
    result = database_connection.execute(text('SELECT 1'))
    assert result.fetchone()[0] == 1
    