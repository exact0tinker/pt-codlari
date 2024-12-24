#alfabetik olarak sıralama
liste=["B","İ","L","İ","Ş","İ","M"]
liste.sort()
print(liste)

#listeyi tersten yazma
liste=["B","İ","L","İ","Ş","İ","M"]
liste.reverse()
print(liste)

#"i"den ne kadar olduğunu bulma
liste=["B","İ","L","İ","Ş","İ","M"]
say=liste.count("İ")
print(say)

#listeyi B,İ,L,İ,M haline getrime
liste=["B","İ","L","İ","Ş","İ","M"]
yeni_liste=[eleman for eleman in liste if eleman in["B","İ","L","M"]]
print("Gerekli harfler ile filtrelenmş liste:", yeni_liste)

#ders listesini alan listesine kopyalama
liste=["B","İ","L","İ","Ş","İ","M"]
alan=liste.copy()
print("Alan listesi:",alan)


#listenin tüm elemanlarını silme
liste=["B","İ","L","İ","Ş","İ","M"]
liste.clear()
print("Tüm elemanları sildikten sonra ders listesi:",liste)



#"L" elemanının indeksini bulma
if "L" in liste:
    index_L=liste.index("L")
else:
    index_L=None
print("L elemanının indeksi:", index_L)



























      
    




