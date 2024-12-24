
kitap_isimleri = ["Kiraz Ağacı", "Endülüs'te Bir Hafta", "Rich Dad Poor Dad", "Kapatuka"]
sayfa_sayilari = [207, 272, 292, 176]

eklenecek_kitap=input("Kitap eklemek ister misiniz")
if eklenecek_kitap=="evet":
   index=int(input("hangi rafa ekleme yapmak istersiniz?"))
   hangi_kitap=input("kitap ismini giriniz")
   kitap_isimleri.insert(index,hangi_kitap)

   kac_sayfa=int(input("eklediğiniz kitap kaç sayfa?"))
   sayfa_sayilari.insert(index,kac_sayfa)
   
   aranacak_kitap = input("Hangi kitabı arıyorsunuz? ")
   
if aranacak_kitap in kitap_isimleri:
    SiraNo=kitap_isimleri.index(aranacak_kitap)
    print(aranacak_kitap, " kütüphanede var", sayfa_sayilari[SiraNo], " sayfadır")
    
else:
    print(aranacak_kitap, "kitabı bizde yoktur.")

print("Kütüphanedeki kitaplar")
print(kitap_isimleri)




