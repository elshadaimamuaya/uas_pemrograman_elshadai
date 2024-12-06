import time
import random
from collections import deque

class Nasabah:
    def __init__(self, nama, prioritas):
        self.nama = nama
        self.prioritas = prioritas
        self.waktu_masuk = time.time()

class Loket:
    def __init__(self, id_loket):
        self.id_loket = id_loket
        self.antrian = deque()
        self.total_layanan = 0
        self.total_waktu_tunggu = 0

    def tambah_nasabah(self, nasabah):
        self.antrian.append(nasabah)

    def layani_nasabah(self):
        if self.antrian:
            nasabah = self.antrian.popleft()
            waktu_tunggu = time.time() - nasabah.waktu_masuk
            self.total_waktu_tunggu += waktu_tunggu
            self.total_layanan += 1
            print(f"Nasabah {nasabah.nama} dilayani di loket {self.id_loket}. Waktu tunggu: {waktu_tunggu:.2f} detik.")
        else:
            print(f"Loket {self.id_loket} tidak ada nasabah dalam antrian.")

    def statistik(self):
        if self.total_layanan > 0:
            rata_waktu_tunggu = self.total_waktu_tunggu / self.total_layanan
            print(f"Loket {self.id_loket} - Total Layanan: {self.total_layanan}, Rata-rata Waktu Tunggu: {rata_waktu_tunggu:.2f} detik.")
        else:
            print(f"Loket {self.id_loket} belum melayani nasabah.")

class SistemAntrian:
    def __init__(self):
        self.lokets = [Loket(i) for i in range(1, 4)]  # 3 loket

    def tambah_nasabah(self, nama, prioritas):
        nasabah = Nasabah(nama, prioritas)
        # Menentukan loket berdasarkan prioritas
        loket_terpilih = min(self.lokets, key=lambda loket: len(loket.antrian))
        loket_terpilih.tambah_nasabah(nasabah)
        print(f"Nasabah {nasabah.nama} dengan prioritas {nasabah.prioritas} ditambahkan ke loket {loket_terpilih.id_loket}.")

    def layani_nasabah(self):
        for loket in self.lokets:
            loket.layani_nasabah()

    def statistik(self):
        for loket in self.lokets:
            loket.statistik()

def main():
    sistem = SistemAntrian()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Nasabah")
        print("2. Layani Nasabah")
        print("3. Statistik Pelayanan")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            nama = input("Masukkan nama nasabah: ")
            prioritas = input("Masukkan prioritas (1-tinggi, 2-sedang, 3-rendah): ")
            sistem.tambah_nasabah(nama, int(prioritas))
        elif pilihan == '2':
            sistem.layani_nasabah()
        elif pilihan == '3':
            sistem.statistik()
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()