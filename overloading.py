class check():
    def product(a,b):
        c = a * b
        print(c)

    def product(a,b,c):
        x  = a+b+c
        print(x)

def main():
    h1 = check()
    h1.product(4,5)
    h1.product(1,2,3)

if __name__ == "__main__":
    main()