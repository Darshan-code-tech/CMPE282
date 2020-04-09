class Computer():

     #self represents the instance of class
     #init method or constructor
    def __init__(self,RAM,Space):
        self.RAM = RAM
        self.Space = Space
    
    def config(self):
        return self.RAM,self.Space
    
com1 = Computer("i6",16)
com2 = Computer("i8",32)

print(com1.RAM,com1.Space)
print(com2.RAM,com2.Space)
