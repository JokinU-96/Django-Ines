def es_gerente(user):
    return user.groups.filter(name='gerente').exists()