def derivative(x, y):
    n=len(x)
    sx, sy, sxx, sxy, s, st=0, 0, 0, 0, 0, 0
    for i in range(n):
        sx +=x[i]
        sxx += x[i]*x[i]
        sy += y[i]
        sxy += x[i]*y[i]
        
    slope = (n*sxy - sx*sy)/(n*sxx - sx*sx)# comes from y=a*x + b fit line
    return slope
    
def wave_function(position, time):
    if  np.dot(derivative(position, time),derivative(position, time))==1:
        print('normalized')
    else:
        print('not-normalized')
def fact(n):
    return 1 if (n==1 or n==0) else n * fact(n - 1)
def taylor(x): #needs some fixing
    x=np.array(x)
    n=len(x)
    tay=[]
    for i in x:
        tay.append((x[i]**n)/fact(n))
    return tay
