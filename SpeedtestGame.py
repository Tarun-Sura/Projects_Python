# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 23:55:19 2020

@author: Tarun
"""

import matplotlib.pyplot as plt
import time as t

times = []
mistakes =0

print("this program will help you type faster. type word programming as fast as u can for 5 times.")
input("press enter to continue")

while len(times)<5:
    start=t.time()
    word = input("Type the word")
    end=t.time()
    time_elapsed =end -start
    
    times.append(time_elapsed)
    
    if(word.lower() != "programming"):
        mistakes=mistakes+1

print("you made"+str(mistakes)+"mistakes")

print("Now lets see your evolution") 

t.sleep(3)

x=[1,2,3,4,5] 
y =times
plt.plot(x,y)
legend =["1","2","3","4","5"]
plt.xticks(x,legend)
plt.ylabel('time in seconds')
plt.xlabel('attempts')
plt.title("your typing evolution")

plt.show()  