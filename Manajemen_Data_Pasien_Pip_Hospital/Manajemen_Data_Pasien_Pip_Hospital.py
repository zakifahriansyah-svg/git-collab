import os # Untuk membersihkan terminal
from colorama import Fore, Style, init # Library untuk mewarnai teks
from tabulate import tabulate # Library untuk tabel
from auth import login
from admin_menu import menu_admin
from info_umum import menu_info_umum
from registrasi import mulai_registrasi
from menu_user import main_menu
import sys # Untuk mengubah runtime
import time # Untuk jeda waktu

init(autoreset=True)

def clear():
    os.system('cls || clear')

def menu_utama():
    current_user = None
    current_role = None

    while True:
        clear()
        print("="*40)
        print("SELAMAT DATANG DI PIP HOSPITAL".center(40))
        print("="*40)
        menu_data = [["1", "Login"], ["2", "Register"], ["3", "Info Umum"], ["4", "Logout"]]
        print(tabulate(menu_data, headers=["No", "Menu"], tablefmt="rounded_outline"))

        pilihan = input("\nPilih menu (1-4): ").strip()
        clear()

        if pilihan == "1":
            result = login()
            if result and result[0]:
                current_user, current_role = result
                if current_role == "admin":
                    menu_admin(current_user)
                    current_user = None
                    current_role = None
                elif current_role == "user":
                    main_menu()
                    current_user = None
                    current_role = None
        elif pilihan == "2":
            mulai_registrasi()  
        elif pilihan == "3":
            menu_info_umum()
        elif pilihan == "4":
            clear()
            print(f"\nSampai jumpa!")
            teks ="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⡀⠀⢄⠈⢙⢒⠲⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⠚⠃⢣⠀⠸⣶⠋⢈⠇⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⠤⢄⡀⠀⠀⢀⣤⣶⢖⣿⣏⡷⠰⠞⠉⠉⢺⣇⠀⢹⠀⢸⡀⠋⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⠤⠶⣚⣋⡅⠀⠀⠙⣻⡟⠋⡔⠛⠉⠁⠙⣷⠀⠰⣿⡄⠀⢻⡆⠀⢧⠀⠙⢦⠀⡿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣯⡵⠛⠛⠉⠈⣷⠀⠘⠉⠀⠙⢦⡀⠀⣾⣆⠀⢻⣇⠀⢳⣳⡀⠘⣷⣀⣨⠙⢲⣒⣤⢣⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡿⡇⢴⠀⠀⣿⠈⣇⠀⢸⣣⡀⠘⣧⡀⠙⠿⠀⠈⣿⣄⣸⡏⢻⣾⣥⢨⣿⣿⠿⠛⠛⠉⠀⠀⣀⣤⣤⠤⠤⣒⡲⠤⠤⣤⣤⣤⣤⣀⡀⢧⡀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠻⡆⢧⠀⠹⡄⢹⡄⠘⢏⢧⠀⢸⡷⣤⣤⣶⣚⠋⢸⠛⢳⣿⡅⠘⢇⢷⣿⠀⠀⣤⢔⣻⡯⠶⠛⠛⠋⠉⠉⠉⠉⣉⣉⣛⡛⠓⢲⣬⡝⣷⣤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⡘⡆⠀⢻⠀⢳⣄⣼⠛⢳⣾⢥⣴⠛⠉⠁⠉⢻⡄⠈⢣⢣⠀⠸⡎⠈⣧⣯⡾⠋⠁⠀⣠⣤⣴⣾⣿⣿⣿⣿⠿⢛⣭⣴⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢧⡛⠀⠚⢰⣿⣿⠛⠳⣼⡇⠀⣿⠀⠘⣟⡄⠈⢳⡀⠘⠿⠃⢠⡇⣠⣿⠛⢀⣤⣾⣿⣿⣿⣿⣿⡿⠟⣫⣤⣞⡯⠚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠛⠪⠖⢻⣝⣦⠀⠘⠇⠀⡟⣦⠀⠛⠿⠀⡼⠓⡦⠤⠴⣫⣤⣿⡁⣠⣿⣿⣿⣿⣿⡿⢿⣡⡴⣿⡭⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢎⠳⡄⠀⠀⡇⢈⣓⣦⡴⢛⡥⣺⡿⠿⢿⣿⣿⠁⣵⣿⣿⣿⡿⠟⣡⣴⣿⣳⣛⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠤⠒⢦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠈⠆⠀⡧⢸⣿⠛⠛⠛⠛⠁⠀⣠⣾⣿⠃⣼⣿⣿⣿⢋⣴⠞⠋⠀⠴⠿⠿⣿⣯⣹⣀⣀⣀⡀⠀⠀⠀⠀⠀⣘⣦⣤⣀⠈⠑⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⣴⣃⡬⣿⣁⡀⠀⠀⠀⣼⣿⢿⡇⡴⠋⠀⣻⡿⠛⠁⠀⠀⠀⠀⠀⠀⠉⢙⣶⡿⠿⠿⠭⣍⣒⣶⢤⣀⣏⣀⠉⠓⣝⡄⠈⢧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢷⡿⠋⢉⣿⠀⢀⣞⡿⠃⠸⠃⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢦⣤⣀⣀⡀⠈⠉⠳⢮⣝⠯⣶⡀⠈⣿⠦⠼⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣰⡟⠀⣰⡿⠋⢹⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⣿⣿⣷⣶⣄⡀⠉⠳⣝⢿⡉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣽⣿⣿⣏⣿⠀⠀⣿⠁⢠⣿⢻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣝⠿⣿⣿⣿⣿⣿⣿⣷⣄⠘⢷⣙⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⡿⠞⠉⠸⢏⣾⡟⠉⢷⡀⣿⣦⣼⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⣶⣌⡙⠿⣿⣿⣿⣿⣿⣷⣄⠻⣍⢦⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⢸⣿⡇⠀⠈⢉⣿⢿⣿⣫⣿⠀⠀⠀⠀⠀⣀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣱⠁⠙⠯⢿⡶⣤⣉⡻⠿⣿⣿⣿⣦⠙⣮⢦⠀⠀⠀
⠀⠀⠀⣴⣿⠟⠀⠀⠀⠀⠀⠀⠘⣟⣇⣀⣶⡯⠟⠋⠉⠀⢹⣆⠀⠀⠀⠀⠻⣦⣄⣀⣤⡶⠀⠀⠀⠀⠀⢐⠶⢀⣴⣿⠁⠀⠀⠀⠀⠉⠙⠯⢽⣷⡶⣍⣙⠻⣷⠈⢯⣣⡀⠀
⠀⠀⡼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠹⣾⣿⣋⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⢀⣀⠀⠘⠷⠛⣿⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠻⢿⣶⣤⣜⢯⣣⡀
⠀⢸⣿⠃⢰⠀⣀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠖⠀⠀⠀⠀⠀⠀⠀⢹⣷⣤⡀⠀⠀⠀⠀⣷⣄⣀⣀⣈⡉⣀⡀⠀⢠⡿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣟⠇⠇
⢀⣿⡟⠀⠀⠀⣿⠀⢰⣇⠀⡴⠂⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠉⠛⠶⣤⣤⡀⠀⠉⠉⠁⠈⠙⢋⣠⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁
⢸⣿⡇⠀⠀⠀⠻⣄⣸⠙⢦⡀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠛⠛⢿⣷⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡇⠀⠀⠀⠀⠙⠋⠀⠀⠹⠀⠀⢸⡿⣦⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠈⢷⣄⢀⣄⢰⣷⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠙⠟⣿⣿⠻⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢷⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠲⣿⠀⠉⠹⣿⣦⠀⠀⠀⠀⠀⠀⢀⡀⢀⣰⣷⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⢟⣷⣄⡀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⢹⣇⠀⠀⠈⢙⣿⣷⡀⠀⢀⣴⣿⣴⣟⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠿⢟⣶⣤⣄⣀⣀⣀⣨⣿⣦⣀⣀⣀⣀⣀⣿⡄⠀⠀⠈⠉⣿⣿⡶⠛⠉⠀⣾⡝⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠒⠚⠛⠓⠊⠉⠿⣿⣿⡋⢹⡁⣸⢷⡄⠀⠀⠀⠸⣆⣀⠀⠀⣾⣽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠯⠭⠭⠭⢽⣿⣦⡀⠰⣄⢺⣿⣆⣾⣽⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠚⠛⠲⣻⣛⣿⡿⣿⣾⡏⠀⠀
"""
            for _ in teks:
                sys.stdout.write(_)
                time.sleep(0.005) 
            print("Stay healthy y'all")
            break
        else:
            print("\nPilihan tidak valid.")
            input(Fore.YELLOW + "Tekan enter untuk melanjutkan..." + Style.RESET_ALL)

if __name__ == "__main__":
    menu_utama()