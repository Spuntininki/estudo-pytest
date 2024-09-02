def valid_email(email):
    return '@' in email and "." in email

def divide(a, b):
    if b == 0:
        return None
    return a / b