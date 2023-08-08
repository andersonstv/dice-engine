from random import randint

class Dice:
    def __init__(self, quantity, sides):
        self.quantity = quantity
        self.sides = sides
        self.result = [randint(1, self.sides) for _ in range(self.quantity)]
    def get_result(self):
        return self.result
    def get_total(self):
        return sum(self.result)
class DiceExp:
    def __init__(self, quantity, sides, **kwargs):
        self.quantity = quantity
        self.sides = sides
        
