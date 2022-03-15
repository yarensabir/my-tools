#!/usr/bin/python3
# -*- coding: utf-8 -*-

#okunacak text dosyalarının olduğu path 
path = "/home/yaren/rb2022/data_eski/robotaksi-data/alan/text/"

counters = [0]*17 #olan class sayısının boyuna göre dizi oluşturuyoruz
for i in range(1,6522): #6522 adet text dosyamız var
    try: 
        #text isimlerimiz 1.txt, 2.text, ... şeklinde
        file =  str(path) + str(i) + ".txt" 
        lines = open(file).readlines()
        for text in lines:
            text, *_ = text.split(" ") #etiketin hangi sınıfa ait olduğunu gösteren sayıları alıyorum
            for j in range(0,17): #bizim 17 adet sınıfımız olduğu için 17
                #okuduğumuz class id ile sayacın index numarası aynı ise sayacı artırıyoruz
                #böyle bir etiketten kaç tane olduğunu saymış oluyoruz
                if text == (str(j)):
                    counters[j] = counters[j] + 1
    except Exception:
        print(i)

for j in range(len(counters)):
    print(str(j+1) +"--->"+  str(counters[j]))





    





