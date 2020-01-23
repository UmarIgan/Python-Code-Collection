
#http://wiki.stat.ucla.edu/socr/index.php/AP_Statistics_Curriculum_2007_Pareto
import math
import random
import statistics 
def cum_density(arr):
    min_value = min(arr)
    mode=statistics.mode(arr)
    emp_list=[]
    for num in arr:
        
        emp_list.append(1- ((min_value/num)**mode))
    return emp_list


o=cum_density(arr)
ind=list(range(0, len(o)))

#draw Cumulative density function
fig = px.line(x=ind, y=o, title='cumilative_density_distrubiton')
fig.show()
#draw your array
fig = px.line(x=ind, y=arr, title='array_distrubiton')
fig.show()
