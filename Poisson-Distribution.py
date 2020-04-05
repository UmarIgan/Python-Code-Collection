from math import exp, factorial
#l: mean value
#k: the number you want to find out the probability of existence
def poisson(k, l):
    return exp(-l)*(((l)**k)/factorial(k))
