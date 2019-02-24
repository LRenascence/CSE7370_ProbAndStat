"""
μ = E(X) = np
σ2 = V(X) = np(1-p) * ( (N - n) / (N - 1) )
p = K / N

"""
def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)

def combination(n, x):
    return factorial(n) / (factorial(x) * factorial(n - x))

def hypergeometricDist(K, N, n, x):
    return combination(K, x) * combination(N - K, n - x) / combination(N, n)

