def calc_discount(value, discount, tax):
    discount_value = value * discount
    tax_value = (value - discount_value)   * tax
    
    return value - discount_value + tax_value



print(calc_discount(100.00, 0.1, 0.05))