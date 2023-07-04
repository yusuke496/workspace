import sys
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import time
import csv

filepath = input("file name: ")
filepath = "data/"+filepath+".csv"
csvdata=[]
data=[]
signal=[]
mean_sig=[]
#step=25
#differential=12500
step = int(input("step: "))
differential = int(input("differential: "))
csvdata = pd.read_csv(filepath, header=0, dtype='float')
data=csvdata.values[:,19]
file_end=len(data)
#print(file_end)

for i in range(0,file_end-step-1):
    if abs(data[i+step]-data[i])<differential:
        #differential=ratio*(data[i+step]-data[i])
        signal.append(data[i])
        #print(data[i])
        i=i+step
    else:
        buf0=len(signal)
        buf1=sum(signal)
        if buf0==0:
            continue
#        print(buf0)
#        print(buf1)
        mean_sig.append(buf1/buf0)
        signal=[]
        i=i+step


mean_sig=np.array(mean_sig)
#mean_sig=mean_sig.reshape(-1,1)
print(mean_sig)
print(len(mean_sig))
x0=[i1 for i1 in range(0,file_end)]
x1=[i1 for i1 in range(0,len(mean_sig))]
fig = plt.figure(figsize=(10, 5))
ax0 = fig.add_subplot(1,1,1)
ax1 = ax0.twiny()
#ax1 = ax0.twinx()
ax0.ticklabel_format(style='sci',axis='x',scilimits=(0,0))
ax0.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
#plt.xlim(0,file_end-1)
#plt.ylim(0,0.4*10**7)
#plt.xticks(np.arange(0, file_end, 200))
#plt.yticks(np.arange(0, 4*10**6, 200000))
ax0.grid()
ax0.plot(x0,data)
ax1.plot(x1,mean_sig)
plt.show()

f = open('signal.csv', 'a')
writer = csv.writer(f, lineterminator='\n')
writer.writerow(mean_sig)
f.close()
