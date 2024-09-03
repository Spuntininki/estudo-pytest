import pytest
from soma import soma

@pytest.mark.parametrize(
    'a, b, expected',
    [
     (1, 2, 3),
     (2, 4, 6),
     (5, 5, 10)
     ]
)
def test_sum(a, b, expected):
    assert soma(a, b) == expected