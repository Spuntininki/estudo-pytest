import pytest
from time import sleep

@pytest.mark.rapido
def test_soma_rapida():
    assert 1 + 2 == 3
    
@pytest.mark.lento    
def test_soma_lenta():
    sleep(2)
    assert 1 + 2 == 3
    
@pytest.mark.rapido
@pytest.mark.lento     
def test_soma_mista():
    sleep(1)
    assert  1 + 2 == 3
    
    
