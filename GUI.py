# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:21:45 2020

@author: DGE
"""
import tkinter as tk
#from tkinter import*
import random
#import pyperclip

def say():
    print("hello world")
def click():
    t = en1.get()
    lb1.config(text=t)
def rand():
    minval = int(en1.get())
    maxval = int(en2.get())
    if minval>maxval:
        temp=minval
        minval=maxval
        maxval=temp
    x = str(random.randint(minval,maxval))
    y = str(random.randint(minval,maxval))
    xshow.config(text="X:" + x)
    yshow.config(text="Y:" + y)
"""def copy():
    xy=xshow.cget("text") +"\n"+ yshow.cget("text") #抓取某部分
    pyperclip.copy(xy)"""

win = tk.Tk() #建立視窗
win.title("tkinter gui") #標題
win.geometry("550x450") # W*H 起始大小
win.minsize(width=550,height=450) # 最小尺寸
win.maxsize(width=1024,height=768)
win.resizable(False,0) # 禁止縮放
win.iconbitmap("work.ico")# ico
win.config(background="skyblue") # 顏色(也可打bg)
win.attributes("-alpha",1) # 1-0 1=不透明 0=透明
win.attributes("-topmost",1) # 至頂 1True 0flase

img = tk.PhotoImage(file="logo.png")
lb_img = tk.Label(image=img)
lb_img.pack()

title_text=tk.Label(text="Random X,Y",bg="skyblue")
# obj.config(font="字型 大小")
title_text.config(font="標楷體 15")
title_text.pack()
#label
lb1=tk.Label(text="min",bg="skyblue",fg="black")
lb1.pack()
#entry(輸入)
en1=tk.Entry()
en1.pack()
#label
lb2=tk.Label(text="max",bg="skyblue",fg="black")
lb2.pack()
#entry(輸入)
en2=tk.Entry()
en2.pack()

#button
btn1 = tk.Button(width=6,height=1,text="Click",bg="gray")
btn1.config(command=rand) # 呼叫funtion
btn1.pack() 
#btn.config(image=img)

"""
btn2 = tk.Button(width=6,height=1,text="Click",bg="gray")
btn2.config(command=copy) # 呼叫funtion
btn2.pack() # pack place grid都可
佈局方式pack grid place
grid(row=0,column=0) #網格佈局位置
place(x=,y=) #座標位置 anchor=方位(N，S，W，E)改變原點位置
"""

xshow = tk.Label(text="",bg="skyblue")
xshow.pack()
yshow = tk.Label(text="",bg="skyblue")
yshow.pack()

win.mainloop() #常駐