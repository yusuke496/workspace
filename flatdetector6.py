import sys
import tkinter
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import time
import csv
import re
import os

#right clic#
def make_menu(w):
    global the_menu
    the_menu = tkinter.Menu(w, tearoff=0)
    the_menu.add_command(label="cut")
    the_menu.add_command(label="copy")
    the_menu.add_command(label="paste")

def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("cut", command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("copy", command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("paste", command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)
#right click
def ButtonEvent(event):
    filepath = EditBox_filepath.get()
    filepath = "data/"+filepath+".csv"
    step_c = EditBox_step.get()
    step = int(step_c)
    differential_c = EditBox_dif.get()
    differential = int(differential_c)
    csvdata=[]
    data=[]
    signal=[]
    mean_sig=[]
    #step=25
    #differential=12500
    #step = int(input("step: "))
    #differential = int(input("differential: "))
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
                #print(buf0)
                #print(buf1)
            mean_sig.append(buf1/buf0/10000000)
            signal=[]
            i=i+step
    mean_sig=np.array(mean_sig)
    EditBox_noe.delete(0, tkinter.END)
    EditBox_noe.insert(tkinter.END, len(mean_sig))
    #mean_sig=mean_sig.reshape(-1,1)
#    print(mean_sig)
#    time.sleep(5)
#    print(len(mean_sig))
    x0=[i1 for i1 in range(0,file_end)]
    x1=[i1 for i1 in range(0,len(mean_sig))]
    fig = plt.figure(figsize=(10, 5))
    ax0 = fig.add_subplot(1,1,1)
    #ax1 = ax0.twinx()
    ax1 = ax0.twiny()
    ax0.ticklabel_format(style='sci',axis='x',scilimits=(0,0))
    ax0.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
    #plt.xlim(0,file_end-1)
    #plt.ylim(0,0.4*10**7)
    #plt.xticks(np.arange(0, file_end, 200))
    #plt.yticks(np.arange(0, 4*10**6, 200000))
    ax0.grid()
    ax0.plot(x0,data)
    ax1.plot(x1,mean_sig*10000000)
    plt.show()

    f = open('signal.csv', 'a')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(mean_sig)
    f.close()

root = tkinter.Tk()
root.title("flat detector")
root.geometry("400x250")

make_menu(root)
root.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

EditBox_filepath = tkinter.Entry(width=40)
EditBox_filepath.insert(tkinter.END,"data")
EditBox_filepath.place(x=50, y=10)

EditBox_step = tkinter.Entry(width=20)
EditBox_step.insert(tkinter.END,"25")
EditBox_step.place(x=50, y=60)

EditBox_dif = tkinter.Entry(width=20)
EditBox_dif.insert(tkinter.END,"12500")
EditBox_dif.place(x=50, y=110)

#左クリック（<Button-1>）されると，ButtonEvent関数を呼び出すようにバインド
EditBox_noe = tkinter.Entry(width=20)
EditBox_noe.insert(tkinter.END," ")
EditBox_noe.place(x=220, y=150)

Button1 = tkinter.Button(text='extract flat', width=15)
Button1.bind("<Button-1>",ButtonEvent)
Button1.place(x=50, y=150)

Button2 = tkinter.Button(text='exit',command=root.quit, width=15)
Button2.place(x=50, y=210)

root.mainloop()
