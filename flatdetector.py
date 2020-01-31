import sys
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import time

filepath = input("file name: ")
filepath = "data/"+filepath
print(filepath)
csvdata=[]
data=[]
signal=[]
i0end=2500
csvdata = pd.read_csv(filepath, header=0, dtype='float')
data=csvdata.values[1:i0end,19]
#print(data)
#sys.exit()
x=[i1 for i1 in range(0,i0end-1)]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(x,data)
ax.grid()
plt.show()
