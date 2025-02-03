def is_prime(numbers):
    a = []
    x = lambda x:[False if (x % i) == 0 else True for i in range(2,x)]
    for number in numbers.split():
        if int(number) != 0 and int(number) != 1:
            a.append(int(number) if False not in x(int(number)) else None)
            if None in a: a.remove(None)
    return a
