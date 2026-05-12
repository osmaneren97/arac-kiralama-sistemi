class Musteri:
    def __init__(self, ad, tc, telefon):
        self.ad = ad
        self.tc = tc
        self.telefon = telefon

    def bilgileri_goster(self):
        print("----------------------")
        print(f"Ad Soyad: {self.ad}")
        print(f"TC: {self.tc}")
        print(f"Telefon: {self.telefon}")