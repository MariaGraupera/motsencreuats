from Taulell import crear_tauler
from Taulell import imprimir_tauler

if __name__ == "__main__":
    # Dimensions del tauler
    filas = 12
    columnas = 12

    # Crear el tauler buit
    tauler = crear_tauler(filas, columnas)

    # Imprimir el tauler buit
    imprimir_tauler(tauler)
