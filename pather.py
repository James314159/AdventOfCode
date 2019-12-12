#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:53:32 2019

@author: ninja
"""

def path_finder(A, B):
    Aplaces = [[0,0]]
    Bplaces =[[0,0]]
    posA = [0,0]
    posB = [0,0]
    for i in A:
        if i[0] == "U":
            for j in range(1, int(i[1:])+1):
                Aplaces.append([posA[0], posA[1]+j])
            posA[1] += int(i[1:])
        if i[0] == "D":
            for j in range(1, int(i[1:])+1):
                Aplaces.append([posA[0], posA[1]-j])
            posA[1] -= int(i[1:])
        if i[0] == "R":
            for j in range(1, int(i[1:])+1):
                Aplaces.append([posA[0] + j, posA[1]])
            posA[0] += int(i[1:])
        if i[0] == "L":
            for j in range(1, int(i[1:])+1):
                Aplaces.append([posA[0] - j, posA[1]])
            posA[0] -= int(i[1:])
    for i in B:
        if i[0] == "U":
            for j in range(1, int(i[1:])+1):
                Bplaces.append([posB[0], posB[1]+j])
            posB[1] += int(i[1:])
        if i[0] == "D":
            for j in range(1, int(i[1:])+1):
                Bplaces.append([posB[0], posB[1]-j])
            posB[1] -= int(i[1:])
        if i[0] == "R":
            for j in range(1, int(i[1:])+1):
                Bplaces.append([posB[0]+ j, posB[1]])
            posB[0] += int(i[1:])
        if i[0] == "L":
            for j in range(1, int(i[1:])+1):
                Bplaces.append([posB[0] - j, posB[1]])
            posB[0] -= int(i[1:])
    apple = [x for x in Bplaces if x in Aplaces]
    print(sorted([abs(pear[0]) + abs(pear[1]) for pear in apple]))
            
            