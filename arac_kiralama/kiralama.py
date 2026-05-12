class Kiralama:
    def __init__(self):
        self.kiralamalar = []

    def arac_kirala(self, arac, musteri, gun):
        if arac.musait:
            arac.musait = False

            toplam_ucret = arac.gunluk_ucret * gun

            bilgi = {
                "musteri": musteri.ad,
                "plaka": arac.plaka,
                "gun": gun,
                "ucret": toplam_ucret
            }

            self.kiralamalar.append(bilgi)

            print("\nAraç başarıyla kiralandı!")
            print(f"Toplam ücret: {toplam_ucret} TL")

        else:
            print("Bu araç şu anda kirada!")

    def arac_teslim(self, arac):
        if not arac.musait:
            arac.musait = True
            print("Araç teslim edildi.")
        else:
            print("Araç zaten müsait durumda.")

    def kiralamalari_listele(self):
        print("\n--- Kiralama Listesi ---")

        if len(self.kiralamalar) == 0:
            print("Kiralama bulunmuyor.")

        else:
            for k in self.kiralamalar:
                print("----------------------")
                print(f"Müşteri: {k['musteri']}")
                print(f"Plaka: {k['plaka']}")
                print(f"Gün Sayısı: {k['gun']}")
                print(f"Toplam Ücret: {k['ucret']} TL")