#listeyi büyükten küçüğe sıralama
liste=["35", "26", "81", "64"]
liste.sort(reverse=True)
print(liste)



#listeyi tersten yazma
liste=["35", "26", "81", "64"]
liste.reverse()
print(liste)



#listede kaç adet 26 elemanı olduğunu bulma
liste=["35", "26", "81", "64"]
say=liste.count("26")
print(say)


#listedeki 81 sayısını silme
liste=["35", "26", "81", "64"]
del liste[2]
print(liste)


#listenin tüm elemanlarını silme
liste=["35", "26", "81", "64"]
liste.clear()
print("Tüm elemanları sildikten sonra ders listesi:",liste)


#64 elemanının indeksini bulma
liste=["35", "26", "81", "64"]
print(liste.index("64"))



#Listeyi ondalikli_sayilar isimli, elemanları 1.4, 6.8 olan liste ile birleştirme
sayilar=["35", "26", "81", "64"]
ondalikli_sayilar=["1.4","6.8"]
sayilar.extend(ondalikli_sayilar)
print(sayilar)










      


