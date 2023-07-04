import numpy as np
from math import sqrt
from qutip import *
import numpy.linalg as LA
import matplotlib.pyplot as plt
import scipy

def drange(begin, end, step):
    n = begin
    while n+step <= end:
        yield n
        n += step

ls=0
a=0
j0=float(input("initial J="))
j1=float(input("final J="))
for q in range(-1,2):
    print("delta m = ",q)
    for m0 in drange(-j0,j0+1,1):
        for m1 in drange(-j1,j1+1,1):
            if clebsch(j0,1,j1,m0,q,m1)!=0:
                print(m0,'->',m1,':',clebsch(j0,1,j1,m0,q,m1)**2)
            a+=clebsch(j0,1,j1,m0,q,m1)**2
print("total = ",a)
