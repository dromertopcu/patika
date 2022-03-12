import time
dic =[]
hesap = []
l = list()
while 3 < 4:
    t = input("Sayı: ")
    start_time = time.time()
    a = range(0,int(t))
    _sinir = len(t)
    us = range(1,_sinir+1)
    num = [0,1,2,3,4,5,6,7,8,9]
    if len(dic)>=(_sinir) :
        for x in a :
            sum = 0
            sayi = list(map(int,str(x)))
            n_sayi = len(sayi)
            for y in sayi :
                item = dic[n_sayi-1][y] 
                sum = sum + item
            if sum == int(x) :
                l[_sinir-1].append(x)
        if l :

            print(l[_sinir-1])
        else :
            print("Sorry maybe next time")

        print("--- %s seconds ---" % (time.time() - start_time))
    else :
        for j in range(len(dic)+1,_sinir+1) :
            for i in num :
                hesap[i:i] = [i**j]
            dic.append(hesap)
            hesap = []
        print("Hesaplama başlıyor")
        for x in a :
            sum = 0
            sayi = list(map(int,str(x)))
            n_sayi = len(sayi)
            for y in sayi: 
                item = dic[n_sayi-1][y] 
                sum = sum + item
            if sum == int(x) :
                l.append([x])
        if l :
            print(l)
        else :
            print("Sorry maybe next time")

        print("--- %s seconds ---" % (time.time() - start_time))