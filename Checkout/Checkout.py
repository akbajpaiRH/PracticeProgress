class Checkout:
    def __init__(self):
        self.items = {}

    def addPrice(self, item, price):
        self.items[item] = price

    def addItem(self,item):
        pass