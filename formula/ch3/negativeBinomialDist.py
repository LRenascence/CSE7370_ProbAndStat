"""
μ = E(X) = r / p
σ2 = V(X) = r(1 - p) / p ** 2

"""

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)

def combination(n, x):
    return factorial(n) / (factorial(x) * factorial(n - x))


def negativeBinomialDist(x, r, p):
    return combination(x - 1, r - 1) * p ** r * (1 - p) ** (x - r)

def cumulativeNegativeBinomialDis(x, r, p, upperLimit):
    count = 0
    while x <= upperLimit:
        count += negativeBinomialDist(x, r, p)
        print(negativeBinomialDist(x, r, p))
        x += 1
    return count
