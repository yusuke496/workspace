import sys
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import time

filepath = input("file name: ")
filepath = "data/"+filepath+".csv"
csvdata=[]
data=[]
signal=[]
i0end=2500
csvdata = pd.read_csv(filepath, header=0, dtype='float')
data=csvdata.values[1:i0end,19]
#print(data)
#sys.exit()
x=[i1 for i1 in range(0,i0end-1)]
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1,1,1)
ax.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
#plt.xlim(0,i0end)
#plt.ylim(0,0.4*10**7)
plt.xticks(np.arange(0, i0end, 200))
plt.yticks(np.arange(0, 4*10**6, 200000))
ax.grid()
ax.plot(x,data)
plt.show()

#for i in range(0,i0end-50):
#    if data[i+50]-data[i]<100000:
#        i=i+1
#        #print(signal)
#    else:
#        signal.append(data[i])
#        print(signal)
#        i=i+1
#print(signal)
