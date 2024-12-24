
kitap_isimleri = ["Kiraz Ağacı", "Endülüs'te Bir Hafta", "Rich Dad Poor Dad", "Kapatuka"]
sayfa_sayilari = [207, 272, 292, 176]

aranacak_kitap = input("Hangi kitabı arıyorsunuz? ")

if aranacak_kitap in kitap_isimleri:
    SiraNo=kitap_isimleri.index(aranacak_kitap)
    print(aranacak_kitap, " kütüphanede var", sayfa_sayilari[SiraNo], " sayfadır")
    
else:
    print(aranacak_kitap, "kitabı bizde yoktur.")






