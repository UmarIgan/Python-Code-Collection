def der(x):#derivative function
    n=len(x)
    y=list(range(n))
    sx, sy, sxx, sxy, s, st=0, 0, 0, 0, 0, 0
    for i in range(n):
        sx +=x[i]
        sxx += x[i]*x[i]
        sy += y[i]
        sxy += x[i]*y[i]
        
    slope = (n*sxy - sx*sy)/(n*sxx - sx*sx)# comes from y=a*x + b fit line
    return slope
def fact(n):
    return 1 if (n==1 or n==0) else n * fact(n - 1)
def f(m):
    return m*der(x) + 0.1#slope function
def taylor(x, a): #needs some fixing
    x=np.array(x)
    element=x[0]
    n=len(x)
    der=derivative(f(x), a, dx=1e-6)
    for j in x:    
        tay=(der/fact(x))*((x[j]-a)**n)
    return tay
