class Animal():
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I am in Human Class and I can move")

class Snake(Animal):
    def move(self):
        print("I am in Snake Class and I can just crawl")

def main():

    h1 = Human()
    h1.move()

    h2 = Snake()
    h2.move()

if __name__ == "__main__":
    main()