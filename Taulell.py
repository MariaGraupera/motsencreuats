def crear_tauler(filas, columnas):
    tauler = [['x' for _ in range(columnas)] for _ in range(filas)]
    return tauler

def imprimir_tauler(tauler):
    for fila in tauler:
        print(' '.join(fila))
