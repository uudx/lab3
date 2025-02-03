x = lambda x, count = 0: [False if (x % i) == 0 else True for i in range(2,x)]
number = int(input())
print("it is a prime number" if False not in x(number) else "it is not a prime number") if number != 0 or 1 else print("it is not a prime number")
