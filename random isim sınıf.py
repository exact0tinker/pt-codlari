import random

sinif_listesi=["İrem Alıç","Melis Doğa","Emre Taş","Enes Taş","Bükre Er","Şakir Güvenç","Yusuf Güllü","Ghaith Kasas","Cem Köse","Ege Tuna","Osman Karaosman","Havin Rezan","Alperen Daş","Yusuf Samet"]

mevcut=len(sinif_listesi)-1      

rastgele=(random.randint(0,mevcut))

print(sinif_listesi[rastgele])

