import pytest
from calc_discount import calc_discount

@pytest.mark.parametrize('value', [10.00, 50.00, 100.00])
@pytest.mark.parametrize('discount', [0.1, 0.05, 0.5])
@pytest.mark.parametrize('tax', [0.02, 0.1, 0.05])
def test_calc_discount(value, discount, tax):
    discount_value = value * discount
    tax_value = (value - discount_value)   * tax
    
    test_final_value = value - discount_value + tax_value
    
    assert calc_discount(value=value, discount=discount, tax=tax) == test_final_value