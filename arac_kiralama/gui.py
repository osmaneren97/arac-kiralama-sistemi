import tkinter as tk
from tkinter import messagebox

# ================== SINIFLAR ==================

class Arac:
    def __init__(self, marka, model, plaka, gunluk_ucret):
        self.marka = marka
        self.model = model
        self.plaka = plaka
        self.gunluk_ucret = gunluk_ucret
        self.musait = True


class Musteri:
    def __init__(self, ad, tc, telefon):
        self.ad = ad
        self.tc = tc
        self.telefon = telefon


class Kiralama:
    def __init__(self):
        self.kiralamalar = []

    def kirala(self, arac, musteri, gun):
        if arac.musait:
            arac.musait = False
            toplam = arac.gunluk_ucret * gun

            self.kiralamalar.append({
                "musteri": musteri.ad,
                "arac": f"{arac.marka} {arac.model}",
                "plaka": arac.plaka,
                "gun": gun,
                "ucret": toplam
            })

            return f"Kiralama başarılı! Toplam ücret: {toplam} TL"
        else:
            return "Bu araç zaten kirada!"


# ================== VERİLER ==================

araclar = [
    Arac("Toyota", "Corolla", "34 ABC 123", 1500),
    Arac("Renault", "Clio", "06 XYZ 789", 1200),
    Arac("BMW", "320i", "35 BMW 35", 3000)
]

sistem = Kiralama()

# ================== ARAYÜZ ==================

root = tk.Tk()
root.title("Araç Kiralama Sistemi")
root.geometry("650x500")
root.config(bg="#2c2f4a")


# BAŞLIK
baslik = tk.Label(root,
                  text="ARAÇ KİRALAMA SİSTEMİ",
                  font=("Arial", 18, "bold"),
                  fg="white",
                  bg="#2c2f4a")
baslik.pack(pady=10)


# ARAÇ LİSTESİ
listbox = tk.Listbox(root, width=70, height=7)
listbox.pack(pady=10)


def listele():
    listbox.delete(0, tk.END)
    for i, a in enumerate(araclar):
        durum = "MÜSAİT" if a.musait else "KİRADA"
        listbox.insert(
            tk.END,
            f"{i+1}. {a.marka} {a.model} | {a.plaka} | {a.gunluk_ucret} TL | {durum}"
        )


listele()


# FORM ALANI
frame = tk.Frame(root, bg="#2c2f4a")
frame.pack(pady=10)

tk.Label(frame, text="Ad Soyad:", fg="white", bg="#2c2f4a").grid(row=0, column=0)
ad_entry = tk.Entry(frame)
ad_entry.grid(row=0, column=1)

tk.Label(frame, text="TC:", fg="white", bg="#2c2f4a").grid(row=1, column=0)
tc_entry = tk.Entry(frame)
tc_entry.grid(row=1, column=1)

tk.Label(frame, text="Telefon:", fg="white", bg="#2c2f4a").grid(row=2, column=0)
tel_entry = tk.Entry(frame)
tel_entry.grid(row=2, column=1)

tk.Label(frame, text="Gün:", fg="white", bg="#2c2f4a").grid(row=3, column=0)
gun_entry = tk.Entry(frame)
gun_entry.grid(row=3, column=1)


# KİRALAMA FONKSİYONU
def kirala():
    secim = listbox.curselection()

    if not secim:
        messagebox.showerror("Hata", "Lütfen araç seç!")
        return

    try:
        gun = int(gun_entry.get())
    except:
        messagebox.showerror("Hata", "Geçerli gün gir!")
        return

    musteri = Musteri(
        ad_entry.get(),
        tc_entry.get(),
        tel_entry.get()
    )

    arac = araclar[secim[0]]
    sonuc = sistem.kirala(arac, musteri, gun)

    messagebox.showinfo("Sonuç", sonuc)
    listele()


# BUTON
btn = tk.Button(root,
                text="ARAÇ KİRALA",
                command=kirala,
                bg="green",
                fg="white",
                font=("Arial", 12, "bold"))
btn.pack(pady=10)


root.mainloop()
