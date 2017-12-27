import numpy as np
inputs=[10,20,30] #layers, inputs, 4,5 6,7
layers=[[[10,20,30]], [[2,-2,1], [3,-4,-1]],[[1,-2], [2,-1]]]
fourw=[2,-2,1]
fivew=[3,4,-1]
sixw=[1,-2]
sevenw=[2,-1]
outputs=[2,1]
dots=[]
As=[]
outputAs=[-10000,-10000]
lamda=0.01
numvectors=7
deltas=[0]*(numvectors-len(outputs)-1)
def back_propagate():
    while abs(outputAs[len(outputAs)-2]-outputs[len(outputs)-2])>0.0001 or abs(outputAs[len(outputAs)-1]-outputs[len(outputs)-1])>0.0001:
        print("reached")
        for l in range(1, len(layers)-1): #goes to all but output layer
            layer=layers[l]
            for j in layer:
     #           numvectors=numvectors+1
                dot = np.dot(j, inputs)
                dots.append(dot)
                As.append(A(dot))
        layer=layers[len(layers)-1]
        oldAs=[]
        for i in range(len(As)):
            oldAs.append(As[i])
        #print(oldAs)
        outputVal=0
        for j in layer:
            dot=np.dot(j, oldAs)
            dots.append(dot)
            As.append(A(dot)) #all dots and As are now done
            outputAs[outputVal]=A(dot)
            outputVal=outputVal+1
            #print(As)
        n=len(dots)-1
        o=len(outputs)-1
        for j in layers[len(layers)-1]:
            deltas[n]=Aprime(dots[n])*(outputs[o]-As[n])
            n=n-1
            o=o-1
        for l in range(len(layers)-1,1,-1):
            newn=n
            nn=n-1 #going from 4 to 5
            #print(newn)
            layer=layers[l]
            start=0
            for i in layer: #w46*delta6 + w47 times delta7
                #print(newn)
                deltas[nn]=Aprime(dots[newn])*summing(start)
                newn=newn-1
                nn=nn+1
                start=start+1
        newAs=[10,20,30]
        newAs.append(As)
        for i in range(1,len(layers)-1):
            layer=layers[i]
            j=0
            for weight in layer:
                i=0
                for val in weight:
                    oldval=val
                    val=oldval+(lamda*newAs[i]*deltas[j])
                    print(val)
                    i=i+1
                j=j+1
        print(outputAs)
        dots.clear()
        As.clear()
        deltas.clear()
        for i in range(len(deltas)):
            delta[i]=0
        oldAs.clear()
    print(outputAs)           
    
def A(num):
    return num/10

def Aprime(num):
    return 0.1

def summing(start):
    w=0
    s=0
    d=numvectors-len(dots)-1
    for j in layers[len(layers)-1]:
        s=s+j[start]*deltas[d]
        d=d+1
    return s


back_propagate()
