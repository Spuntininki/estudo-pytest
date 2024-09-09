import pytest
import time

def soma(a, b):
    return a + b

def multiplica(a, b):
    return a * b

@pytest.mark.lento
def test_soma_lenta():
    time.sleep(2)
    assert 4 == soma(2, 2)

@pytest.mark.rapido
def test_soma_rapida():
    assert 5 == soma(2, 3)

@pytest.mark.lento
def test_multiplicacao_lenta():
    time.sleep(2)
    assert 6 == multiplica(2, 3)

@pytest.mark.rapido
def test_multiplicacao_rapida():
    assert 6 == multiplica(2, 3)
