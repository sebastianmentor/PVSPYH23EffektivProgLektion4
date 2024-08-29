import dis

def list_comprehension():
    resultat = [x**2 for x in range(10)]
    return resultat

dis.dis(list_comprehension)