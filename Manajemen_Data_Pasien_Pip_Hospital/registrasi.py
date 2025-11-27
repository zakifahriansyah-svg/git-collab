import os # Untuk membersihkan terrminal
import pandas as pd # Untuk manipulasi data
from InquirerPy import inquirer
from pwinput import pwinput # Agar password tidak terlihat di terminal
from colorama import Fore, Style, init # Untuk mewarnai teks
init(autoreset=True)

dataDIR = 'data'
users_file = f'{dataDIR}/users.csv'
autentikasi = "admin123"

def clear():
    os.system('cls || clear')

def load_users():
    if not os.path.exists(users_file):
        return {}
    df = pd.read_csv(users_file, dtype=str)
    return {
        row["username"]: {"password": row["password"], "role": row["role"]}
        for _, row in df.iterrows()
    }

def save_users(users):
    df = pd.DataFrame([
        {"username": u, "password": d["password"], "role": d["role"]}
        for u, d in users.items()
    ])
    df.to_csv(users_file, index=False)

def mulai_registrasi():
    users = load_users()

    print("="*50)
    print("SILAKAN BUAT AKUN BARU".center(50))
    print("="*50)

    # Input username
    while True:
        username = input("Username: ").strip()
        if not username:
            print(Fore.RED + "Username tidak boleh kosong!" + Style.RESET_ALL)
        elif username in users:
            print(Fore.RED + "Username sudah digunakan. Coba yang lain!" + Style.RESET_ALL)
        else:
            break

    # Input password
    password = pwinput("Password: ").strip()
    if not password:
        print(Fore.RED + "Password tidak boleh kosong!" + Style.RESET_ALL)
        input(Fore.YELLOW + "Tekan enter untuk melanjutkan..." + Style.RESET_ALL)
        clear()
        return

    # Pilih role dengan inquirer
    pilihan_role = inquirer.select(
        message="Pilih role:",
        choices=["User Biasa", "Admin", "Batal"],
        pointer="➡️ ",
        qmark=""
    ).execute()

    if pilihan_role == "Batal":
        print("Registrasi dibatalkan.")
        input(Fore.YELLOW + "Tekan enter untuk melanjutkan..." + Style.RESET_ALL)
        clear()
        return
    elif pilihan_role == "Admin":
        role = "admin"
        print("\nDiperlukan kode rahasia untuk membuat akun admin.")
        kode = pwinput("Masukkan kode rahasia: ").strip()
        if kode != autentikasi:
            print(Fore.RED + "Kode salah! Registrasi admin dibatalkan." + Style.RESET_ALL)
            input(Fore.YELLOW + "Tekan enter untuk melanjutkan..." + Style.RESET_ALL)
            clear()
            return
    else:
        role = "user"

    # Simpan akun baru
    users[username] = {"password": password, "role": role}
    save_users(users)

    print(Fore.GREEN + f"\nAkun '{username}' berhasil dibuat sebagai {role}!" + Style.RESET_ALL)
    input(Fore.YELLOW + "Tekan enter untuk melanjutkan..." + Style.RESET_ALL)
    clear()