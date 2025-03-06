def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El factorial solo está definido para enteros no negativos.") # raise es para lanzar excepciones de manera manual
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n < 1:
        raise ValueError("El índice debe ser un entero positivo.")
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for i in range(0, 11):
        print(f"{i}! = {factorial(i)}")

    for i in range(1, 11):
        print(f"fibonacci_{i} = {fibonacci(i)}")