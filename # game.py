# game.py
# Bilgisayar 1-100 arasında rastgele bir sayı tutar, kullanıcı doğru tahmin edene kadar devam eder.

import random

print("Tahmin Oyunu")
print("Bilgisayar 1 ile 100 arasında bir sayı tuttu.")
print("Doğru sayıyı bulmak için tahmin yap!")

# Rastgele sayı üret
sayi = random.randint(1, 100)
tahmin_sayisi = 0

while True:
    try:
        tahmin = int(input("Tahmininizi girin: "))
        tahmin_sayisi += 1

        if tahmin < sayi:
            print("Daha büyük bir sayı söyleyin ")
        elif tahmin > sayi:
            print("Daha küçük bir sayı söyleyin ")
        else:
            print(f" Tebrikler! {tahmin_sayisi}.denemede doğru tahmin ettiniz!")
            break
    except ValueError:
        print("Hata")
