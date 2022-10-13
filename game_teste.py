

listas = [0, 5, 10, 15, 20, 25, 30]

def filtro(numero):
    if numero > 10:
        return True
    return False

listas_filtrada = filter(filtro, listas)