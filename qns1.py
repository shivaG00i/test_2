# Base class for family members
class FamilyMember:
    def __init__(self, name, behavour):
        self.name = name
        self.behavour = behavour

    def argue(self, opponent):
        pass 

    def cal(self, behavour):

        if self.behavour == behavour:
            return "Draw"
        elif (self.behavour == "Arrogant" and behavour > "Calm"):
            return "Arrogant"
        elif (self.behavour == "Rebellious" and behavour > "Arrogant"):
            return "Rebellious"
        elif (self.behavour == "Stubborn" and behavour > "Rebellious"):
            return "Stubborn"
        elif (self.behavour == "Calm" and behavour > "Stubborn"):
            return "Calm"
        else:
            return " loses"


class Father(FamilyMember):
    def __init__(self,behavour):
        super().__init__("Father", "Arrogant")

    def argue(self, opponent):
        pass

class Mother(FamilyMember):
     def __init__(self ,behavour):
        super().__init__("Mother", "Calm")

   


class Son(FamilyMember):
     def __init__(self,behavour ):
        super().__init__("Son", "Rebellious")

   
class Daughter(FamilyMember):
     def __init__(self,behavour):
        super().__init__("Daughter", "Stubborn")

   