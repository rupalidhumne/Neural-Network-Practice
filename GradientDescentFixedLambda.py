#gradient  of function
#point x and you keep subtract the gradient from it times lambda
#do that until gradient is basically 0

import numpy as np
import matplotlib.pyplot as plt
lam=0

def evaluate(point):
    x=point[0]
    y=point[1]
    return np.array([float((8*x)-(3*y)+24),float((-3*x) + (4*y) + 20)])
    
def descent():
    point=np.array([float(0),float(0)]) #point vector
    g=np.array([float(10),float(10)]) #gradient vector
    iterations=0
    while g[0]>0.001 and g[1]>0.001: 
        #print(point)
        g=evaluate(point) #run 1 d minimization knowing the point and the gradient
        #print(g)
        point[0]=point[0]-g[0]*lam
        point[1]=point[1]-g[1]*lam
        iterations=iterations+1
    print(str(point[0]) + " " + str(point[1]))



def onedmin(function,interval):
    a=interval[0]
    d=interval[1]
    if abs(interval[0]-interval[1])<0.001:
        print(int(function(interval[0]))) #base case if I've gotten to the same point then return function
    else:
        if m(a,function)==True:
            print(a,function(a))
        elif m(d,function)==True:
            print(d,function(d))
        else: 
            b=a/2
            c=d/2
            print(b)
            print(c) #will have to use lambda to change point and basically find the function in part 4
            if b>c:
                return onedmin(function,[c,b])
            else:
                return onedmin(function, [b,c])
def m(val,func):
    if 2*val==0:
        #becuase 2 is positive we already know it's going to be a min
        return True
    return False

def testfunc(x):
    return x**2

#optimization(testfunc, [-2,2])  
 #optimization takes in an interval, while distance is not equal to zero of that interval, check if there's a minimum else shrink the interal      
#PART 3: get point get gradient 1d min returns lambda use that new lambda for gradient descent until I get to the bottom


def descent_three():
    arrx=[]
    arry=[]
    lam=0.01
    while lam<1:
        #print(lam)
        point=np.array([float(0),float(0)]) #point vector
        g=np.array([float(10),float(10)]) #gradient vector
        iterations=0
        while g[0]**2 + g[1]**2 >0.000001: 
            g=evaluate(point)
            #print(g)
            point[0]=point[0]-g[0]*lam
            point[1]=point[1]-g[1]*lam
            iterations=iterations+1
        arrx.append(lam)
        lam=lam+0.01
        arry.append(iterations)
    plt.plot(arrx,arry)
    plt.show()
 

def descent_four(): #dynamic lambda because my point changes each time
    arrlam=[]
    lam=0
    point=np.array([float(0),float(0)]) #point vector
    g=np.array([float(10),float(10)]) #gradient vector
    iterations=0
    while g[0]**2 + g[1]**2 >0.000001:
        g=evaluate(point) #run 1 d minimization knowing the point and the gradient
        lamda=onedmin_four(ev, [0.01,0.5], point,g) #each lamda
        #print(lamda)
        point[0]=point[0]-g[0]*lamda
        point[1]=point[1]-g[1]*lamda
        iterations=iterations+1
    print(point)
    print(iterations)
    print(arrlam)

def ev(pt):
    return (4*pt[0]**2) -(3*pt[0]*pt[1])+(2*pt[1]**2)+(24*pt[0])-(20*pt[1])
def onedmin_four(ev,interval,point, g):
    a=interval[0]
    d=interval[1]
    if abs(a-d)<0.000000000001:
        print(a)
        return a
    else: 
        b=(d-a)*(1/3)+a
        c=(d-a)*(2/3)+a
        #print(b)
        #print(c)
        newpoint1=[-1,-1]
        newpoint2=[-1,-1]
        newpoint1[0]=point[0]-g[0]*b
        newpoint1[1]=point[1]-g[1]*b
        newpoint2[0]=point[0]-g[0]*c
        newpoint2[1]=point[1]-g[1]*c
        n1=ev(newpoint1)
        print("    n1",n1)
        n2=ev(newpoint2)
        print("     n2",n2)
        print("   g", g)
        if n1>n2:
                return onedmin_four(ev,[b,d],point,g)
        else:
            return onedmin_four(ev, [a,c],point,g)

#descent_three()
descent_four()#RETURNS 177 trials
#0.02,0.6
#

        #print(str(point[0]) + " " + str(point[1]))
#ANSWER: -6.78230872369 -10.086396019



