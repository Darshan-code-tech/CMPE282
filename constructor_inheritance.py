class A:
    def __init__(self):
        print("In class A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("In clss B init")

b = B()
