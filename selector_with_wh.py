#!/usr/bin/python3
# -*- coding: utf-8 -*-

def selector_with_wh(path1, path2,  fileCount, filter):
    filter = int(filter)
    for i in range(1,fileCount+1):
        try: 
            file =  path1 + str(i) + ".txt" 
            lines = open(file).readlines()
            for text in lines:
                id, x, y, w, h = text.split(" ") 
                w = float(w) * 1000
                h = float(h) * 1000
                wh = int(w*h)
                if wh >= filter:
                    dosya = path2 + str(i) + ".txt"
                    with open(dosya, 'a') as f:
                        f.write(text)           
        except Exception:
            pass