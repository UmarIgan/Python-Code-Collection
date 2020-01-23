
#http://wiki.stat.ucla.edu/socr/index.php/AP_Statistics_Curriculum_2007_Pareto
import statistics
import collections
def cum_density(arr):
    arr=collections.Counter(arr)
    min_value = min(arr.values())
    mode=statistics.mode(arr.values())
    emp_list=[]
    for num in arr:
        
        emp_list.append(1- ((min_value/num)**mode))
        dictionary = dict(zip(emp_list, arr.values()))
        
    return dictionary

arr=[3, 4, 6, 2, 5, 3, 6, 4, 6, 6, 9, 8, 7]
cum_density(arr)


