import pytest
from classify_age import classify_age

@pytest.mark.parametrize(
    'age, expected',
    [
        (10, 'Criança'),
        (15, 'Adolescente'),
        (23, 'Adulto'),
        (70, 'Idoso')
    ]
)
def test_classify_age(age, expected):
    assert classify_age(age) == expected