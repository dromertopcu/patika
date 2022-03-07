t = input("Sayı :")
sinir = int(t)
a = range(0,sinir)
_range = list(map(int,str(sinir)))
_sinir = len(_range)
us = range(1,_sinir)
num = [0,1,2,3,4,5,6,7,8,9]
dic =[] 
hesap = []
dic = []
for j in us :
    for i in num :
        hesap[i:i] = [i**j]
        print(hesap)
    dic.append(hesap)
    hesap = []
    print(dic)
print("Hesaplama başlıyor")
for x in a :
    _sum = list()
    i = -1
    sayi = list(map(int,str(x)))
    n_sayi = len(sayi)
    for p in sayi:
        i +=1
        _sum[i:i] =[p**n_sayi]
        if sum(_sum) == x :
            l.append(x)
        sayi1 = sayi
        n_sayi1 = n_sayi
        _sum1 = _sum

if l :
    print(l)
    
else :
    print("Sorry maybe next time")

print("--- %s seconds ---" % (time.time() - start_time))