class Arac:
    def __init__(self, marka, model, plaka, gunluk_ucret):
        self.marka = marka
        self.model = model
        self.plaka = plaka
        self.gunluk_ucret = gunluk_ucret
        self.musait = True

    def bilgileri_goster(self):
        durum = "Müsait" if self.musait else "Kirada"

        print("----------------------")
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Plaka: {self.plaka}")
        print(f"Günlük Ücret: {self.gunluk_ucret} TL")
        print(f"Durum: {durum}")