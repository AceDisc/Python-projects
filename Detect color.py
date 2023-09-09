# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:13:10 2018

@author: AceDisc
"""
import pickle
import pyautogui
import time
#Loading Colors Dictionary
load=open("colors.pickle","rb")
Colors=pickle.load(load)
load.close()
#Delay and reading color
time.sleep(5)
(x,y)=pyautogui.position()
c=pyautogui.pixel(x,y)
#Calculating RGB percentages
c=(c[0]*100//255,c[1]*100//255,c[2]*100//255)
print("RGB =",c)
#Checking for exact match
if c in Colors :
    print("Exact match :",Colors[c])
else:
    col=list(c)
    #function for finding closest color
    f = lambda a,l:min(l,key=lambda x:sum(tuple(abs(i-j) for i,j in zip(x,a))))
    l=Colors.keys()
    closest=f(col, Colors.keys())
    print('Closest match found :',closest,':',Colors[closest])
    
