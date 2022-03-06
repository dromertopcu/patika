import time
start_time = time.time()
a = range(0,100000)
l = list()
print("Hesaplama başlıyor")
for x in a:
    sum = 0
    sayi = list(map(int,str(x)))
    n_sayi = len(sayi)
    for y in sayi:
        sum = sum + y**n_sayi
    if sum == int(x) :
        l.append(x)
if l :
    print(l)
    
else :
    print("Sorry maybe next time")

print("--- %s seconds ---" % (time.time() - start_time))