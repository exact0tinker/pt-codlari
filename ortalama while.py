toplam=0
sayac=0
while True:
    sayi=float(input("sayı giriniz"))
    if sayi==1:
      break

    toplam+=sayi
    sayac+=1

print("ortalama",toplam/sayac)
    
    
