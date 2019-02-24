"""
μ = E(X) = 1 / p
σ2 = V(X) = (1 - p) / p ** 2
"""
def geometricDistribution(x, p):
    return p * (1 - p) ** (x - 1)

def cumulativeGeometricDist(x, p, upperLimit):
    count = 0
    while x <= upperLimit:
        count += geometricDistribution(x, p)
        x += 1
    return count

