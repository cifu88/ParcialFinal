#Clase de usuario según diagrama de clases.

from datetime import date
import string


class User(): 
    UserId : string
    Password : string
    RegisterDate : date

    def __init__(self, userId, password):
        self.UserId = userId
        self.Password = password
        print("Ha iniciado sesión con exito")
