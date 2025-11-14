class order():
    def __init__(self,item, price):
        self.price = price
        self.item = item
    def __gt__(self,other):
        return self.price > other.price
order1 = order("Laptop", 75000)
order2 = order("Phone", 55000)

print(order.__gt__(order1,order2))