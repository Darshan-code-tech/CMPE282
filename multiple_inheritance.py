class A:
    def classa(self):
        print("I am in class A")

class B:
    def classb(self):
        print("I am in class B")

class D:
    def classd(self):
        print("I am in class D")

class C(A,B,D):
    def classc(self):
        print("In class C")

c = C()
c.classa()
c.classb()
c.classc()
c.classd()