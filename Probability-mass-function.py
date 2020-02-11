import numpy as np
   
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
def prob_mass(X, event_k):
    for i in event_k:
        return ((np.mean(X)**event_k[i])*np.exp(-np.mean(X)))/factorial(event_k[i])
 
