import random

class Apples:
    jabka=0
    waga=0
    
    def __init__(self,apple):
        self.apple=apple
        Apples.jabka += 1
        Apples.waga += apple
        
while Apples.waga <300 and Apples.jabka <1000:
    Apples(random.uniform(0.2,0.5))
    

print("Liczba jabłek: ", Apples.jabka)
print("WAGA: ", Apples.waga)