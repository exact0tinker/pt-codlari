mars="""Korkma, sönmez bu şafaklarda yüzen al sancak
Sönmeden yurdumun üstünde tüten en son ocak.
O benim milletimin yıldızıdır, parlayacak
O benimdir, o benim milletimindir ancak.
Çatma, kurban olayım çehreni ey nazlı hilâl
Kahraman ırkıma bir gül… ne bu şiddet bu celâl
Sana olmaz dökülen kanlarımız sonra helâl,
Hakkıdır, Hakk’a tapan, milletimin istiklâl."""

TemizlenecekKarakterler=[",",".","?","!",";"]
for Degis in TemizlenecekKarakterler:
    mars=mars.replace(Degis,"")

Kelimeler=mars.split()
aranan=input("hangi kelimeyi aratmak istersiniz?")
bulunanSayisi=0
ToplamKelimeSayisi=0

for Kelime in Kelimeler:
    ToplamKelimeSayisi+=1
    if(Kelime == aranan):
        BulunanSayisi+1
print("Bu metinde ",ToplamKelimeSayisi,"kelime var,aradığınız",aranan,"bu kelimeden",bulunanSayisi,"adet")
