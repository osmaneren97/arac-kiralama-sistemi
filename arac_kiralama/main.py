from arac import Arac
from musteri import Musteri
from kiralama import Kiralama


arac1 = Arac("Toyota", "Corolla", "34 ABC 123", 1500)
arac2 = Arac("Renault", "Clio", "06 XYZ 789", 1200)
arac3 = Arac("BMW", "320i", "35 BMW 35", 3000)

sistem = Kiralama()

while True:
    print("\n===== ARAÇ KİRALAMA SİSTEMİ =====")
    print("1- Araçları Listele")
    print("2- Araç Kirala")
    print("3- Araç Teslim Et")
    print("4- Kiralama Geçmişi")
    print("5- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        arac1.bilgileri_goster()
        arac2.bilgileri_goster()
        arac3.bilgileri_goster()

    elif secim == "2":
        print("\nHangi aracı kiralamak istiyorsunuz?")
        print("1- Toyota Corolla")
        print("2- Renault Clio")
        print("3- BMW 320i")

        arac_secim = input("Araç seçiniz: ")

        if arac_secim == "1":
            secilen_arac = arac1

        elif arac_secim == "2":
            secilen_arac = arac2

        elif arac_secim == "3":
            secilen_arac = arac3

        else:
            print("Geçersiz seçim!")
            continue

        ad = input("Müşteri adı: ")
        tc = input("TC Kimlik No: ")
        telefon = input("Telefon: ")
        gun = int(input("Kaç gün kiralanacak: "))

        musteri = Musteri(ad, tc, telefon)

        sistem.arac_kirala(secilen_arac, musteri, gun)

    elif secim == "3":
        print("\nTeslim edilecek araç:")
        print("1- Toyota Corolla")
        print("2- Renault Clio")
        print("3- BMW 320i")

        teslim_secim = input("Araç seçiniz: ")

        print("Hatalı seçim yaptınız!")