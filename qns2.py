import random

class FamilyMember:
    def __init__(self, name, trait) :
        self.name =  name
        self.trait = trait


class Wife(FamilyMember):
    def __init__(self):
        super().__init__("Wife", "Angry + Arrogant")

    def fight(self):
      
        v = random.randint(10, 30)
        return f'decrease by {v}'


class Husband(FamilyMember):
    def __init__(self):
        super().__init__("Husband", "tolerate")

    def tolerate(self):
        
        v = 5
        return f' increase by {v}'


class FamilyHouse:
    happiness=random.randint(1, 100)
    for i in range(11):
        if happiness<=0:
            print("Divorce")
        else:
            print(" husband tolerates.")  

    