
from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        return randint (1,self.sides)
    
die=Die()
for i in range(10):
    print(die.roll_die())
die10=Die(sides=10)
for i in range(10):
    print(die10.roll_die())
die20=Die(sides=20)
for i in range(10):
    print(die20.roll_die())


