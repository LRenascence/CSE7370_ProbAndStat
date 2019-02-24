"""
μ = E(X) = np
σ2 = V(X) = np(1-p)

"""

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)

def combination(n, x):
    return factorial(n) / (factorial(x) * factorial(n - x))


def binomialDist(n, x, p):
    return combination(n, x) * p ** x * (1 - p) ** (n - x)

def cumulativeBinomialDistribution(n, x, p, upperLimit):
    count = 0
    while x <= upperLimit:
        count += binomialDist(n, x, p)
        x += 1
    return count
