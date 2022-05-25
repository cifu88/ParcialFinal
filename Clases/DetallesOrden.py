import string
from tokenize import Double
from Orden import Orden

class OrderDetails():
    OrderId : OrderId
    ProductId : string
    ProductName : string
    Quantity : int
    UnitCost : Double
    Total : Double

    def __init__(self, orderId):
        self.OrderId = orderId
    
    def CalculateTotal(self):
        print("Su orden tiene un valor de: ")

