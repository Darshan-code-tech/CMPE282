class Employee():
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    
emp1 = Employee("Darshan","Mandlecha",50000)
Employee.set_raise_amt(2)

print(emp1.raise_amt)




