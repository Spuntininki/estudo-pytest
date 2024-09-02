def is_positive(num):
    return num > 0

def test_is_positive_function():
    assert is_positive(5) is True
    assert is_positive(-5) is False