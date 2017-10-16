import numpy as np
import math
import printingGraph as plt

#------------- Parameters ---------------
u = 1

deltaX = 0.01
deltaT = 0.001

time = 1
n = time/deltaT
scale = 10
_j = scale/deltaX

xj = np.arange(0, scale, deltaX)
tn = np.arange(0, time, deltaT)

#------------supporting functions----------------
def functi(q):
    return (q-5)*(q-5) + 3

def distriFun(q):
    return u*q

def supportFun(a,b):
    a_i = (distriFun(b)-distriFun(a))/(b-a)
    F = 1/2 * (distriFun(a)+distriFun(b)) - 1/2*math.fabs(a_i)*(b-a)
    return F

def printFun(i):
    print(density)
    if(i%50==0):
        plt.makePlot(xj, density, str("asd"+str(i)))

density = [functi(q) for q in xj]

def mainFun():
    for i in range(len(tn)):
        for j in range(len(xj)):
            if(j==0 or j==len(xj)-1):
                density[j] = density[j]
            else:
                density[j] = density[j] - deltaT/deltaX * (supportFun(density[j],density[j+1]) - supportFun(density[j-1],density[j]))
                #density[j] = density[j] - deltaT/deltaX * (u*density[j]-u*density[j-1])
        printFun(i)

# ------------------------ Main -----------------------
plt.makePlot(xj, density, str("asd"+str(-1)))
mainFun()
