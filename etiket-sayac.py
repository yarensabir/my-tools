#!/usr/bin/python3
# -*- coding: utf-8 -*-

from array import *

def readTXT(path, fileCount, classCount,):
    counters = [0]*classCount
    for i in range(1,fileCount):
        try: 
            file =  path + str(i) + ".txt" 
            lines = open(file).readlines()
            for text in lines:
                text, *_ = text.split(" ") 
                for j in range(0,classCount): 
                    if text == (str(j)):
                        counters[j] = counters[j] + 1
        except Exception:
            print(i)
    return counters



    





