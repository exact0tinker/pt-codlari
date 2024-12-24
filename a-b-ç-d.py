harf_secimi=input("harf seçiniz (A/C/Ç)?")

if harf_secimi=="A":
 toplam=0
sayi1 = int(input("İlk sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin:"))
if sayi2 < sayi1:
 sayi1, sayi2 = sayi2, sayi1
for sayilar in range(sayi1 + 1, sayi2):
 toplam +=sayilar
print(f"{sayi1} ile {sayi2} arasındaki sayıların toplamı: {toplam}")
'''
if harf_secimi=="Ç":
 toplam=0
sayilar = [4, 12, 18, 33]
for sayi in sayilar:
 toplam += sayi
print("Listedeki elemanların toplamı:", toplam)

if harf_secimi=="C":
 carpım=1
sayi1=int(input("1.sayıyı giriniz:"))
sayi2=int(input("2.sayıyı giriniz:"))
for sayilar in range (sayi1,sayi2):
    carpim*=sayilar
print(carpim)
'''



