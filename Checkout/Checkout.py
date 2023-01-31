class Checkout:
    class Discount:
        def __init__(self,n,price):
            self.n=n
            self.price=price
    def __init__(self):
        self.prices={}
        self.discounts={}
        self.items = {}

    def addPrice(self, item, price):
        self.prices[item] = price

    def addItem(self,item):
        if item in self.items:
            self.items[item]+=1
        else:
            self.items[item]=1
    def calculateTotal(self):
        total=0
        for item,cnt in self.items.items():
            if item in self.discounts:
                discount = self.discounts[item]
                if cnt >= discount.n:
                    nD=cnt/discount.n
                    total = nD * discount.price
                    rem=cnt%discount.n
                    total+=rem*self.prices[item]
                else:
                    total+=cnt * self.prices[item]
            else:
                total+=self.prices[item] * cnt
        return total

    def addDiscount(self,item,n,price):
        discount= self.Discount(n,price)
        self.discounts[item]=discount