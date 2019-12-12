#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:09:42 2019

@author: ninja
"""

def summer(y):
    c=0
    for i in range(len(y)):
        a = str(y[i])
        if c % 4 == 0:
            if a[-2:] == "99":
                break
            elif a[-1:] == "1":
                c += 1
                if len(a) == 4:
                    if a[1] == "1":
                        y[y[i+3]] = int(y[i+2]) + int(y[i+1])
                    else:
                        y[y[i+3]] = int(y[i+2]) + int(y[y[i+1]])
                if len(a) == 3:
                    y[y[i+3]] = int(y[i+1]) + int(y[y[i+2]])
                if len(a) == 1:
                    y[y[i+3]] = int(y[y[i+1]]) + int(y[y[i+2]])
                            
   
            elif a[-1:] == "2":
                c += 1
                if len(a) == 4:
                    if a[1] == "1":
                        y[y[i+3]] = int(y[i+2]) * int(y[i+1])
                    else:
                        y[y[i+3]] = int(y[i+2]) * int(y[y[i+1]])
                if len(a) == 3:
                    y[y[i+3]] = int(y[i+1]) * int(y[y[i+2]])
                if len(a) == 1:
                    y[y[i+3]] = int(y[y[i+1]]) * int(y[y[i+2]])
                
                
            elif a == "3":
                c+=3
                y[y[i+1]] = input("gimme")
            elif a == "4":
                c+=3
                print(y[y[i+1]])
        else:
            c+=1