import matplotlib.pyplot as plt
import numpy as np
n=6 #number of array items
x=[24, 32, 40, 48, 64, 80] #example data with distance and speed of an object
y=[4, 6, 10, 12, 18, 27]
def least_square_fitting():
    
    xi=[]# create an empty array
    
    sx, sy, sxx, sxy, s, st=0, 0, 0, 0, 0, 0
    for i in range(n):
        sx +=x[i]
        sxx += x[i]*x[i]
        sy += y[i]
        sxy += x[i]*y[i]
        
    a = (n*sxy - sx*sy)/(n*sxx - sx*sx)# comes from y=a*x + b fit line 
    b = (sxx*sy - sx*sxy)/(n*sxx - sx*sx)
    for i in range(0, n):
        s += pow((y[i] - a*x[i])-b, 2)#square sum
        st += pow(y[i] - (sx/n), 2)
    for i in range(n):
        xii=b + a*x[i]
        xi.append(xii)
    r2=(st-s)/st#r square
    
    print("coeff1:", a,"coeff2:", b, "square sum:",  s, "r square:", r2 )
    plt.plot(x, y, '.')
    plt.plot(x, xi, '-')
    plt.show()
    
    """
    Least square method is a basic method to find a fitting line of a linear-like data. 
    For more info check: http://www.wiki-zero.co/index.php?q=aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvTGVhc3Rfc3F1YXJlcw 
    is a good start for understanding regression in the machine learning.
    Also check this website for more clear understanding:
    http://www1.gantep.edu.tr/~bingul/ep208/docs/ep208-topic7.pdf .
    The aim of this work is to show how easy python for statistics. 
    You can try your own data but if it is not linear it can't give you the line you wish.
    """

