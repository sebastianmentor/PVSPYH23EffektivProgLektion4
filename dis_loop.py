import dis

def for_loop():
    resultat = []
    for x in range(10):
        resultat.append(x**2)
    return resultat

dis.dis(for_loop)
