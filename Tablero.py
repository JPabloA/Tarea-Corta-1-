
from Ficha import *

class Tablero:

    # Defina aquí los atributos de Tablero
    numeroCasillas = 0
    fichas = []


    # también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil),
    # y un mecanismo para saber quién sigue en el turno

    # agregue parámetros necesarios después de self
    # para iniciar los valores de sus atributos

    def __init__(self):
        player1 = Ficha("rojo")
        player2 = Ficha("azul")
        self.numeroCasillas = 100
        self.fichas = [player1, player2]
        self.fichaActual = 0
        self.gameLogic()


# inicialice aquí todos los atributos
# no olvide usar self.atributo para acceder el atributo de la clase
# defina aquí los métodos de Tablero
# recuerde que el primer parámetro de cada método es siempre self

    def gameLogic(self):
        ronda = 1
        while self.fichas[0].posicion < self.numeroCasillas and self.fichas[1].posicion < self.numeroCasillas:
            print("")
            print("Ronda", ronda)
            print("Ficha de color", self.fichas[0].color + ": ", end='')
            self.fichas[0].avanzar()
            print("Ficha de color", self.fichas[1].color + ": ", end='')
            self.fichas[1].avanzar()
            ronda += 1

        print("")
        if self.fichas[0].posicion >= self.numeroCasillas:
            print("Felicidades, la ficha de color", self.fichas[0].color, "es la ganadora del juego")
        elif self.fichas[1].posicion >= self.numeroCasillas:
            print("Felicidades, la ficha de color", self.fichas[1].color, "es la ganadora del juego")


prueba = Tablero()