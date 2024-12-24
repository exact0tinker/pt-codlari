def basamak_ayirma(sayi):
  """
  Verilen 4 basamaklı bir sayıyı basamaklarına ayırır ve her bir basamağı ekrana yazdırır.

  Args:
    sayi: 4 basamaklı bir tam sayı

  Returns:
    None
  """

  if 1000 <= sayi <= 9999:
    binler = sayi // 1000
    yuzler = (sayi % 1000) // 100
    onlar = (sayi % 100) // 10
    birler = sayi % 10
    print("Binler basamağı:", binler)
    print("Yüzler basamağı:", yuzler)
    print("Onlar basamağı:", onlar)
    print("Birler basamağı:", birler)
  else:
    print("Lütfen 4 basamaklı bir sayı giriniz.")

sayi = int(input("4 basamaklı bir sayı giriniz: "))

basamak_ayirma(sayi)
