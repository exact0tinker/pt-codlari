yas = int(input("Yaşınız kaç? "))
if yas < 20:
    puan = 100
elif 20 <= yas < 40:
    puan = 50
else:
    puan = 30
    
 ev_var = input("Eviniz var mı? (Evet/Hayır): ")
if ev_var == "evet":
        puan += 30
    
    araba_var = input("Arabanız var mı? (Evet/Hayır): ")
if araba_var == "evet":
        puan += 50
    
 marka = input("Arabanızın markası nedir? ")
if marka == "togg":
        puan += 100
elif marka == "tofaş":
        puan += 30
else:
        puan += 50
    
 print(f"Toplam puanınız: {puan}")
