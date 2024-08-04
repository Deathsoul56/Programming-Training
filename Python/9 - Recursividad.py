def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for i in range(0, 11):
        print(f"{i}! = {factorial(i)}")

    for i in range(1, 11):
        print(f"fibonacci_{i} = {fibonacci(i)}")