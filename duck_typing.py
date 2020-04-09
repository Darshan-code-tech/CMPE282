'''
Ducktyping : where the type or the class of an object is less important than the method it defines
'''
class A:
    def execute(self):
        print("Its like interface in Java")
        print("Its duck-typing in Python")
    
class B:
    def execute(self):
        print("Its like interface in Java")     
        print("Its duck-typing in Python")
        print("Java and Python are different")

class check:
    def code(self,ide):
        ide.execute()

ide1 = B()
check1 = check()
check1.code(ide1)
print("===============================")
ide2 = A()
check2 = check()
check2.code(ide2)