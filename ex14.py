def fib(int):
    if (int == 0 or int == 1):
        return int
    else:
        return fib(int-1)+fib(int-2)

for i in range(0,20):
    print(fib(i))
