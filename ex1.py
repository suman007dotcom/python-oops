class soilder():    
    def __init__(self,name,strength,stamina):
        self.name = name
        self.strength = strength
        self.stamina = stamina
    def report(self):
        print(f"{self.name} has strength {self.strength} and stamina {self.stamina}")
Soilder1 = soilder("Arjun",85,90)
Soilder1.report()