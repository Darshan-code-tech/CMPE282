class Solution:
    def fizzBuzz(self, n: int):
        list = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                list.append("FizzBuzz")
            elif i % 5 == 0:
                list.append("Buzz")
            elif i % 3 == 0:
                list.append("Fizz")
            else:
                list.append(str(i))
        
        return list

if __name__ == "__main__":
    x1 = Solution()
    print(x1.fizzBuzz(15))

