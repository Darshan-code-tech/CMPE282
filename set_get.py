class Getter_Setter(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__var = 13

    def college(self):
        print(self.name , self.age)
    
    def setter(self,nums):
        self.__var = nums

    def getter(self):
        return self.__var    
        
if __name__ == "__main__":
    c1 = Getter_Setter("Darshan",18)
    print(c1.name,c1.age)
    
    
    
'''
#if __name__ == "__main__":
c1 = Getter_Setter("Darshan",18)
print(c1.age)
print(c1.name)
c1.__var = 20
print("Check getter_setter : ", c1.__var)
c1.age = 20
print("New Age is : ", c1.age)
c1.college()
'''    
    