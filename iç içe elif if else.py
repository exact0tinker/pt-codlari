sinema_tiyatro=input("tiyatro mu yoksa sinema mı izlemek istesiniz(tiyatro/sinema):")
ogrenci_mi=input("öğrenci misiniz?")
tutar=0
if sinema_tiyatro=="sinema":
    tutar+=15
    if ogrenci_mi=="evet":
       tutar=tutar/2
elif sinema_tiyatro=="tiyatro":
    tutar+=10
    if ogrenci_mi=="evet":
       tutar=tutar/2
print(tutar)
  
                         
                         
