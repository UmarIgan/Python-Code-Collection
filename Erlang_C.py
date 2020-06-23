#A:intensity
#N:num_of_agents
#p: probability of a call wait
from math import factorial
def erlang_c(a, n):
    z=0
    x=((a**n)/factorial(n))*(n/(n-a))
    for i in range(n):
        z+=(a**i)/factorial(i)
    p=x/(z + x)
    return p
