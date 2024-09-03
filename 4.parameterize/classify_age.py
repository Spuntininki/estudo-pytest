def classify_age(age):
    if age < 12:
        return 'Criança'
    elif age < 18:
        return 'Adolescente'
    elif age < 60:
        return 'Adulto'
    else:
        return 'Idoso'