import numpy as np
#from math import sqrt
from qutip import *
#import numpy.linalg as LA
import matplotlib.pyplot as plt
import time

#def drange(begin, end, step):
#    n = begin
#    while n+step <= end:
#        yield n
#        n += step

#def ket(l,lm):
#    nl=int(2*l+1)
#    nm=int(l-lm)
#    return basis(nl,nm)

#def ket2(j,jm,i,im):
#    nl0=int(2*j+1)
#    nm0=int(j-jm)
#    nl1=int(2*i+1)
#    nm1=int(i-im)
#    print(nl0,nm0,nl1,nm1)
#    return tensor(basis(nl0,nm0),basis(nl1,nm1))

#def j2ls(j,jm,l,s):
#    n=0
#    a=[[] for i in drange(0,(2*l+1)*(2*s+1),1)]
#    for i in drange(-l,l+1,1):
#        for k in drange(-s,s+1,1):
#            a[n]=np.dot(clebsch(l,s,j,i,k,jm),tensor(ket(l,i),ket(s,k)))
#            n=n+1
#    return a

jj=3
ii=4.5
ll=2
ss=1
gJ=1+(jj*(jj+1)+ss*(ss+1)-ll*(ll+1))/(2*jj*(jj+1))
muB=1.4
a=-157
b=-9
def H1(x):
    return muB*gJ*x*tensor(jmat(jj,"z"),qeye(int(2*ii+1)))

H2=a*(0.5*(tensor(jmat(jj,"+"),jmat(ii,"-"))+tensor(jmat(jj,"-"),jmat(ii,"+")))+tensor(jmat(jj,"z"),jmat(ii,"z")))

H3=b*(6*(0.5*(tensor(jmat(jj,"-"),jmat(ii,"+"))+tensor(jmat(jj,"+"),jmat(ii,"-")))+tensor(jmat(jj,"z"),jmat(ii,"z")))*(0.5*(tensor(jmat(jj,"-"),jmat(ii,"+"))+tensor(jmat(jj,"+"),jmat(ii,"-")))+tensor(jmat(jj,"z"),jmat(ii,"z")))+3*(0.5*(tensor(jmat(jj,"-"),jmat(ii,"+"))+tensor(jmat(jj,"+"),jmat(ii,"-")))+tensor(jmat(jj,"z"),jmat(ii,"z")))-2*ii*(ii+1)*jj*(jj+1)*tensor(qeye(int(2*jj+1)),qeye(int(2*ii+1))))/(2*ii*(2*ii-1)*2*jj*(2*jj-1))

n0=0
nst=int((2*jj+1)*(2*ii+1))
nend=1000
noffset=0
Hmat=np.zeros((nend,nst,nst))
a=np.zeros((nend,nst))
#print(a)
start=time.clock()
for n in range(nend):
    if (n+1)%100==0:
        print(n+1)
    a[n][:]=(H1(n+noffset)+H2+H3).eigenenergies()
#print(a)
t=time.clock()-start
print(t)
x=np.arange(noffset,noffset+nend,1)
#plt.plot(x,a,color="black",marker=".",markersize=1)
#plt.plot(x,a,color="k")
plt.plot(x,a)
plt.show()
