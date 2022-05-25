import string
from Usuario import Usuario

class Administrator(Usuario):
    Name = string
    Email = string

    def __init__(self):
        print("Se han actualizado los productos con exito")