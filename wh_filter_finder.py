#!/usr/bin/python3
# -*- coding: utf-8 -*-

def wh_finder(path,file_number):
    file =  path + str(file_number) + ".txt" 
    lines = open(file).readlines()
    for text in lines:
        id, x, y, w, h = text.split(" ") 
        w = float(w)* 1000
        h = float(h) * 1000
        wh = int(w*h)
    return wh