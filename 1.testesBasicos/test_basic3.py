from functions import valid_email, divide

def test_valid_email():
    assert valid_email('email@email.com') == True
    assert valid_email('emailInvalido') == False
    assert valid_email('email.Invalido') == False
    assert valid_email('email@Invalido') == False


def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == None