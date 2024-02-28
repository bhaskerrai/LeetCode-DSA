def fn(i):
    if i > 3:
        return

    print(i)
    fn(i + 1)

    print("End of call where i:", i)
    return

fn(1)

# fibonacciNumber returns the nth Fibonacci number (0 indexed)
def fibonacciNumber(n):
    if n <= 1:
        return n

    print(n,"\n")
    oneBack = fibonacciNumber(n - 1)
    print("second wala")
    twoBack = fibonacciNumber(n - 2)
    print("tesre mein")

    print("ab sum hoga: ", oneBack + twoBack)

    return oneBack + twoBack

print(fibonacciNumber(4))


def factorial(i: int):
    if i < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if i == 0 or i == 1:
        return 1
        
    # print(i)
    return i * factorial(i - 1)

# print(factorial(3))