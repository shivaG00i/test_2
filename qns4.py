class Investment:
    def __init__(self, name, amount, growth_rate):
        self.name = name  
        self.amount = amount  
        self.growth_rate = growth_rate  


class House(Investment):
    def __init__(self, amount):
        super().__init__("House", amount, 0.05)  

class Gold(Investment):
    def __init__(self, amount):
        super().__init__("Gold", amount, 0.08)  

class Land(Investment):
    def __init__(self, amount):
        super().__init__("Land", amount, 0.12) 

class Stocks(Investment):
    def __init__(self, amount):
        super().__init__("Stocks", amount, 0.15) 



class Future(Investment):
    def future_value(self, years):
        values= self.amount * (1 + self.growth_rate) ** years
        return values

class FatherPortfolio:

    def simulate(self, years):
       pass


