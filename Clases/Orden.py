from datetime import date
import string
from unicodedata import name
from Cliente import Cliente

class Order():
    OrderId : string
    Date : date
    CustomerName : CustomerName
    CustomerId : CustomerId

    def __init__(self, customerName, customerId):
        self.CustomerId = customerId
        self.CustomerName = customerName
    
    def PlaceOrder(self):
        print("Su orden ya fue adjuntada")