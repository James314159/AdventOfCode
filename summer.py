#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:09:42 2019

@author: ninja
"""

def summer(y):
    c=0
    for i in range(len(y)):
        if c % 4 == 0:
            if y[i][-2:] == "99":
                break
            elif y[i][-2:] == "1":
                c += 1
                if len(y[i][:-2]) == 3:
                    if y[i][:-2][1] == "1":
                        y[y[i+3]] = str(int(y[i+2]) + int(y[i+1]))
                    else:
                        y[y[i+3]] = str(int(y[i+1]) + int(y[y[i+2]]))
                if len(y[i][:-2]) = 2:
                    if y[i][:-2][1] == "1":
                        y[y[i+3]] = str(int(y[i+2]) + int(y[y[i+1]]))
                    else:
                        y[y[i+3]] = str(int(y[y[i+1]]) + int(y[y[i+2]]))
                if len(y[i][:-2]) = 0:
                    y[y[i+3]] = str(int(y[y[i+1]]) + int(y[y[i+2]]))
                            
   
            elif y[i][-2:] == "2":
                c += 1
                if len(y[i][:-2]) == 3:
                    if y[i][:-2][1] == "1":
                        y[y[i+3]] = str(int(y[i+2]) * int(y[i+1]))
                    else:
                        y[y[i+3]] = str(int(y[i+1]) * int(y[y[i+2]]))
                if len(y[i][:-2]) = 2:
                    if y[i][:-2][1] == "1":
                        y[y[i+3]] = str(int(y[i+2]) * int(y[y[i+1]]))
                    else:
                        y[y[i+3]] = str(int(y[y[i+1]]) * int(y[y[i+2]]))
                if len(y[i][:-2]) = 0:
                    y[y[i+3]] = str(int(y[y[i+1]]) * int(y[y[i+2]]))
                
                
            elif y[i] == "3":
                c+=3
                y[y[i+1]] = input("gimme")
                print("ooh")
            elif y[i] == "4":
                c+=3
                print(y[i+1])
        else:
            c+=1