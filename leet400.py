class Employee():

    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"
    
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def raise_pay(self):
        return self.pay * self.raise_amount

dev1 = Employee("Darshan","Mandlecha",50000)

print(dev1.raise_pay())

class Developer(Employee):
    def __init__(self,first,last,pay,program_language):
        super().__init__(first,last,pay)
        self.program_language = program_language

    raise_amount = 1

dev2 = Developer("Darshan2","M",40000,"Python")

print(dev2.raise_pay())
print(dev2.fullname())