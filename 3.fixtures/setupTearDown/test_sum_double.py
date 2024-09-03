import pytest

def sum_double(numeros):
    return sum(x * 2 for x in numeros)


@pytest.fixture
def generated_list():
    return [2, 4, 8, 16, 32]

def test_sum_double(generated_list):
    input_list = generated_list
    output_sum = sum_double(input_list)
    
    assert output_sum == 124
        
def test_sum_double_zero(generated_list):
    generated_list.clear()
    output_sum = sum_double(generated_list)
    
    assert output_sum == 0
        
