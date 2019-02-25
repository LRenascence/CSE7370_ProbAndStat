import math

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)

def poissonDist(Lambda, x):
    return math.e ** (-Lambda) * Lambda ** x / factorial(x)