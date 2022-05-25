#Ejercicio de herencia:

from datetime import date
import string


class Persona():
    nombre = string
    nif = string
    fechaNac = date


class jugador(Persona):
    numFed : int

