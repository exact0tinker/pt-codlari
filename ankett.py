                         #ELİF İLE İŞLEMLER
yas = int(input("Yaşınızı girin: "))
ev_var = input("Eviniz var mı? (Evet/Hayır): ")
araba_var = input("Arabanız var mı? (Evet/Hayır): ")
puan = 0

if yas < 20:
    puan += 100
elif yas <40:
    puan+=50
else:
    puan+=30
if ev_var == "Evet":
    puan += 30
if araba_var == "Evet":
    puan += 50

    arac_turu = input("Aracınızın markası nedir? (Togg/Tofaş/Diğer): ")
    if arac_turu == "Togg":
        puan += 100
    elif arac_turu == "Tofaş":
        puan += 30
    if arac_turu=="Diğer":
        puan+=50

print(f"Toplam puanınız: {puan}")
