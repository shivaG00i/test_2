import random

  

def calculate():

   
   
    for week in range(1, 5):
       for i in range(random.randint(1, 3)):
        v=random.randint(1, 3)
        yield v
        total_bottles += v
       

    if total_bottles <= 4:
        return "Health is safe"
    elif 5 <= total_bottles <= 8:
        return "Mild damge"
    elif 9 <= total_bottles <= 12:
        return "Severe damage "
    else:
        return "Critical condition  "



