import time
start_time = time.time()
a = range(0,100000000)
_range = list(map(int,str(100000000)))
_sinir = len(_range)
us = range(1,_sinir)
num = [0,1,2,3,4,5,6,7,8,9]
dic =[] 
hesap = []
dic = []
l = list()
for j in us :
    for i in num :
        hesap[i:i] = [i**j]
    dic.append(hesap)
    hesap = []
print("Hesaplama başlıyor")
item = dic[0][8]
for x in a :
    sum = 0
    sayi = list(map(int,str(x)))
    n_sayi = len(sayi)
    for y in sayi: 
        item = dic[n_sayi-1][y] 
        sum = sum + item
    if sum == int(x) :
        l.append(x)
if l :
    print(l)
else :
    print("Sorry maybe next time")

print("--- %s seconds ---" % (time.time() - start_time))