import time
start_time = time.time()
a = range(0,10000000)
l = list()
n_sayi1 = -1
sayi1 = -1
print("Hesaplama başlıyor")
for x in a:
    _sum = list()
    i = -1
    sayi = list(map(int,str(x)))
    n_sayi = len(sayi)
    if n_sayi == n_sayi1 :
        for p, k in zip(sayi, sayi1):
            i +=1
            if p == k :
                _sum.insert(i,_sum1[i])
            else :
                _sum[i:i] =[p**n_sayi]
        if sum(_sum) == x :
            l.append(x)
        sayi1 = sayi
        n_sayi1 = n_sayi
        _sum1 = _sum
    else :
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