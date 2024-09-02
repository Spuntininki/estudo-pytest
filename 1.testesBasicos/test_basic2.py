def subtract(a, b):
    return a - b

def get_list_length(list):
    return len(list)


def test_subtract_and_list_length():
    assert subtract(5, 1) == 4
    assert get_list_length([1, 2, 3]) == 3