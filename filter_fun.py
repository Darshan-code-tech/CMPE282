def fun(var):
    letter = ['a','e','i','o','u']
    if var in letter:
        return True
    else:
        return False

if __name__ == "__main__":
    sequence = ['w','d','e','i']
    filtered = filter(fun,sequence)
    for i in filtered:
        print(i)