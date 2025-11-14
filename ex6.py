class avg_marks():
    def __init__(self, name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    
    @property
    def percentage(self):
        avg = (self.marks1 + self.marks2 + self.marks3)/3
        return avg

makr=avg_marks("syman",1,1,1)
print(makr.percentage)