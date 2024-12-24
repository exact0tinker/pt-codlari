sayi1=int(input("Birinci sayıyı girin: "))
sayi2=int(input("İkinci sayıyı girin: "))
islem=input("İşlem seçin (+,-,*,/): ")
if islem=="+":
    sonuc=sayi1+sayi2
    print(sonuc)
elif islem=="-":
    sonuc=sayi1-sayi2
    
elif islem=="*":
    sonuc=sayi1*sayi2
    print(sonuc)
elif islem=="/":
    sonuc=sayi1/sayi2
    print(sonuc)  
else:
    print("Yanlış işlem girdiniz")
