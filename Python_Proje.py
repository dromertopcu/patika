'''
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
'''

def flatten_input_user() :
    print("[" + input("Listenizi giriniz: ").strip().replace('[', '').replace(']', '') + "]")


def flatten(x) :
    l = []
    for i in x :
        if type(i) == list :
            for j in i :
                if type(j) == list :
                    for k in j :
                        if type(k) == list :
                            for m in k :
                                l.append(m)
                        else :
                            l.append(k)
                else:
                    l.append(j)
        else:
            l.append(i)
    print(l)

task1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flatten(task1)

def reverser(x) :
    l = [i[::-1] if type(i) == list else i for i in x[::-1]  ]
    print(l)

task2 = [[1, 2], [3, 4], [5, 6, 7]]

reverser(task2)
