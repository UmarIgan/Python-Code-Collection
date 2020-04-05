from statistics import mean
from math import exp, factorial

def prob_mass(X, event_k):
    for i in event_k:
        return ((mean(X)**event_k[i])*exp(-mean(X)))/factorial(event_k[i])
 
