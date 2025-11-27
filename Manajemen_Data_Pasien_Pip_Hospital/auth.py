import os # Untuk memberrsihkan terminal
import pandas as pd # Untuk memanipulasi data
from pwinput import pwinput # Agar password tidak terlihat di terminal
from colorama import Fore, Style, init # Untuk mewarnai teks
from registrasi import mulai_registrasi
init(autoreset=True)

dataDIR = ('data')
users_file = (f'{dataDIR}/users.csv')

def clear():
    os.system('cls || clear')

def load_users():
    df = pd.read_csv(users_file, dtype=str)
    if df.empty:
        return {}   
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

def login():
    users = load_users()
    for kesempatan in range(3):
        try:
            print("="*50)
            print("SILAKAN LOGIN DENGAN AKUN ANDA".center(50))
            print("="*50)
            username = input("Username: ").strip()
            password = pwinput("Password: ").strip()

            if username in users and users[username]["password"] == password:
                role = users[username]["role"]
                print(Fore.GREEN + f"\nLogin sebagai {username} berhasil" + Style.RESET_ALL)
                input(Fore.YELLOW + "Tekan enter untuk melanjutkan..." + Style.RESET_ALL)
                clear()
                return username, role
            else:
                sisa = 2 - kesempatan
                if sisa >= 0:
                    print(Fore.RED + f"\nLogin gagal! Sisa percobaan: {sisa}")
                    input(Fore.YELLOW + "Tekan enter untuk melanjutkan..." + Style.RESET_ALL)
                    clear()
                else:
                    break
        except Exception as e:
            print(f"\nError: {e}")
            input(Fore.YELLOW + "Tekan enter untuk melanjutkan..." + Style.RESET_ALL)
            clear()

    print(Fore.RED + "Anda sudah gagal login sebanyak 3 kali." + Style.RESET_ALL)
    print(Fore.RED + "Mengalihkan ke menu registrasi..." + Style.RESET_ALL)
    input(Fore.YELLOW + "Tekan enter untuk melanjutkan..." + Style.RESET_ALL)
    clear()
    mulai_registrasi()
    return None, None