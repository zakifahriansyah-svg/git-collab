import os
import csv # Mengimport file csv yang ada di dalam folder data
from InquirerPy import inquirer # Library pointer
from tabulate import tabulate # Library untuk tabel
from colorama import Fore, Style, init # Library untuk mewaarnai teks

init(autoreset=True) # Reset colorama

dataDIR = 'data' # Memanggil data dalam folder data
dfPasien = f'{dataDIR}/pasien.csv'
dfInfoUmum = f'{dataDIR}/info_umum.csv'
dfInfoDokter = f'{dataDIR}/info_dokter.csv'

def baca_csv(path_file): # Fungsi untuk membaca csv
    with open(path_file, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def clear(): # Fungsi membersihkan terminal
    os.system("cls || clear")

def tampilkan_tabel(data):
    headers = list(data[0].keys())
    rows = [list(row.values()) for row in data]
    headers_warna = [Fore.CYAN + h + Style.RESET_ALL for h in headers]
    print(tabulate(rows, headers=headers_warna, tablefmt="rounded_outline"))
    print()

def menu_info_umum():
    while True:
        clear()
        pilihan = inquirer.select(
            "Pilih menu:",
            choices=[
                "1. Lihat Jadwal Besuk",
                "2. Lihat Jadwal Dokter",
                "Keluar"
            ],
            pointer="➡️ ",
            qmark=""
        ).execute() 

        if pilihan == "1. Lihat Jadwal Besuk":
            clear()
            print("="*60)
            print("JADWAL BESUK".center(60))  
            print("="*60)
            data = baca_csv(dfInfoUmum)
            tampilkan_tabel(data)
            input(Fore.YELLOW + "Tekan enter untuk melanjutkan..." + Style.RESET_ALL)
        elif pilihan == "2. Lihat Jadwal Dokter":
            clear()
            print("="*85)
            print("JADWAL DOKTER".center(85)) 
            print("="*85)
            data = baca_csv(dfInfoDokter)
            tampilkan_tabel(data)
            input(Fore.YELLOW + "Tekan enter untuk melanjutkan..." + Style.RESET_ALL)
        elif pilihan == "Keluar":
            print(Fore.GREEN + "Kembali ke menu utama..." + Style.RESET_ALL)
            break 
