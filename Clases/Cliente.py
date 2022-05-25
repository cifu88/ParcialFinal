from audioop import add
import string
from tokenize import Double
from Usuario import Usuario

class Customer(Usuario):
    CustomerName : string
    Address : string
    Email : string
    CustomerId : string
    AccountBalance : Double

    def register(self, name, address, email, customerId, accountBalance):
        self.Name = name
        self.Address = address
        self.Email = email
        self.CustomerId = customerId
        self.AccountBalance = accountBalance
        print("Se ha registrado con exito")
    
    def purchase(self):
        print("Compra realizada con exito")


