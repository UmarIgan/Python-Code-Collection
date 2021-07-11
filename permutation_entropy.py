#for more: https://www.aptech.com/blog/permutation-entropy/#mjx-eqn-compute_PE

from math import factorial, log2

def permutation_entropy(time_series):
    freq_list = []
    for entry in time_series: #calculating frequency of each element in time series
        counter = 0.
        for i in time_series:
            if i == entry:
                counter += 1
        freq_list.append(float(counter) / len(time_series))
        
        perm_ent=0
        for i in freq_list:
             perm_ent+= -i*log2(i)
        
        perm_ent_norm=0
        for i in freq_list:
            perm_ent_norm+=((1/log2(factorial(len(time_series))))*-i*log2(i))
       
    return perm, perm_ent_norm #returns permutation entropy and normalized permutation entropy
