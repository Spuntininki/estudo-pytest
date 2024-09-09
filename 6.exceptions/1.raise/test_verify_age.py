import pytest

def verify_age(age):
    if age < 18:
        raise ValueError('Acesso negado. Menor de idade.')
    return 'acesso permitido'


def test_veryfy_age_exception():
    
    with pytest.raises(ValueError):
        verify_age(17)
        
        
@pytest.mark.parametrize('age', (20, 18, 30))
def test_veryfy_age(age):
    assert verify_age(age) == 'acesso permitido'
    
    
def test_verify_age_exception_message():
    with pytest.raises(ValueError) as e:
        verify_age(10)
        assert 'Acesso negado. Menor de idade.' in str(e)