def temp():
    list = [1,5,2,4,3,2]
    target = 6
    start = 0
    end = len(list) -1
    res = []
    while (start < end):
        if list[start] + list[end] == target:
            res.append((list[start], list[end])) 
        start += 1
        end -= 1
    return res
    
if __name__ == '__main__':
    resp = temp()
    print(resp)